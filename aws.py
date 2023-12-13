#!/usr/bin/env python3
import boto3
import xlsxwriter
import json
from creds import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN
identstoreid = "d-96671a6efc"
instancearn = "arn:aws:sso:::instance/ssoins-8210d427f0325278"

def get_session():
    return boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, aws_session_token=AWS_SESSION_TOKEN)

def get_all_groups(identstore):
    groups_resp = identstore.list_groups(IdentityStoreId=identstoreid)
    groups = groups_resp["Groups"]
    next_token = groups_resp.get("NextToken")
    while next_token:
        groups_resp = identstore.list_groups(IdentityStoreId=identstoreid, NextToken=next_token)
        groups += groups_resp["Groups"]
        next_token = groups_resp.get("NextToken")

    return groups

def get_all_permissionsets(ssoadmin):
    resp = ssoadmin.list_permission_sets(InstanceArn=instancearn)
    next_token = resp.get("NextToken")
    permissionsets = resp.get("PermissionSets")
    while next_token:
        resp = ssoadmin.list_permission_sets(InstanceArn=instancearn, NextToken=next_token)
        next_token = resp.get("NextToken")
        newpermissionsets = resp.get("PermissionSets")
        permissionsets += newpermissionsets
    return permissionsets


def get_permissionsets_from_account(ssoadmin, accountid):
    resp = ssoadmin.list_permission_sets_provisioned_to_account(AccountId=accountid, InstanceArn=instancearn)
    next_token = resp.get("NextToken")
    permissionsets = resp.get("PermissionSets")
    while next_token:
        resp = ssoadmin.list_permission_sets_provisioned_to_account(AccountId=accountid, InstanceArn=instancearn, NextToken=next_token)
        next_token = resp.get("NextToken")
        newpermissionsets = resp.get("PermissionSets")
        permissionsets += newpermissionsets
    return permissionsets

def get_permissionsets_name(ssoadmin, arn):
    resp = ssoadmin.describe_permission_set(InstanceArn=instancearn, PermissionSetArn=arn)
    return resp["PermissionSet"]["Name"]

def get_group_members(identstore, group_id):
    membership_resp = identstore.list_group_memberships(IdentityStoreId=identstoreid, GroupId=group_id)
    members = membership_resp["GroupMemberships"]
    user_names = []
    for member in members:
        userid = member["MemberId"]["UserId"]
        user_resp = identstore.describe_user(IdentityStoreId=identstoreid, UserId=userid)
        username = user_resp["UserName"]
        user_names.append(username)
    return user_names

def get_inline_policy(ssoadmin, perm_set_arn):
    resp = ssoadmin.get_inline_policy_for_permission_set(InstanceArn=instancearn, PermissionSetArn=perm_set_arn)
    try:
        inline_policy = json.loads(resp.get("InlinePolicy"))
        return inline_policy
    except json.decoder.JSONDecodeError:
        return dict()

def get_s3_permission_from_inline_policy(inline_policy):
    all_permission = []
    try:
        for statement in inline_policy.get("Statement"):
            permission = []
            if statement["Effect"] == "Allow":
                if type(statement["Action"]) == str:
                    permission.append("*")
                elif type(statement["Action"]) == list:
                    for action in statement["Action"]:
                        if action.startswith("s3:"):
                            permission.append(action.replace("s3:",""))
            else:
                continue
            if len(permission) == 0:
                continue
            if type(statement["Resource"]) == str:
                if statement["Resource"].startswith("arn:aws:s3:::"):
                    statement["Resource"] = statement["Resource"].replace("arn:aws:s3:::","")
                elif statement['Resource'] != "*":
                    statement["Resource"] = "no buckets"
                permission.append(f"Buckets : {statement['Resource']}")
            elif type(statement["Resource"]) == list:
                rsrc = []
                for resource in statement['Resource']:
                    if resource.startswith('arn:aws:s3:::'):
                        rsrc.append(resource.replace('arn:aws:s3:::',''))
                    elif resource == "*":
                        rsrc.append("*")
                if len(rsrc) == 0:
                    rsrc = ["no buckets"]
                permission.append(f"Buckets : {', '.join(rsrc)}")
            else:
                print("ERROR")
                print(permission["Resource"])
            all_permission.append(", ".join(permission[:-1]) + f" ({permission[-1]})")
    except TypeError:
        pass
    except Exception as e:
        print("ERROR!")
        print(e)
    if len(all_permission) == 0:
        return "No inline policy for s3 found"
        
    return "\n".join(all_permission)


def get_all_aws_accounts(org):
    resp = org.list_accounts()
    accounts = resp["Accounts"]
    next_token = resp["NextToken"]
    while next_token:
        resp = org.list_accounts(NextToken=next_token)
        accounts += resp["Accounts"]
        next_token = resp.get("NextToken")
    return accounts

def write_to_excel(title, **contents):
    workbook = xlsxwriter.Workbook(f'output-{title}.xlsx')
    for sub in contents:
        worksheet = workbook.add_worksheet(sub)
        content = contents[sub]
        for row in range(len(content)):
            for col in range(len(content[row])):
                worksheet.write(row, col, str(content[row][col]))
    workbook.close()

def write_groups_and_members(identstore):
    all_groups = get_all_groups(identstore)
    groups_and_members = [("Groups", "Members")]
    i = 1
    for group in all_groups:
        print(group["DisplayName"], i)
        i+=1
        groupid = group["GroupId"]
        members = ", ".join(get_group_members(identstore, groupid))
        groups_and_members.append((group["DisplayName"], members))
    
    write_to_excel("groups_and_members", groups_and_members=groups_and_members)
    # workbook = xlsxwriter.Workbook(f'groups_and_members.xlsx')
    # worksheet = workbook.add_worksheet()
    # for row in range(len(groups_and_members)):
    #     for col in range(len(groups_and_members[row])):
    #         worksheet.write(row, col, groups_and_members[row][col])
    # workbook.close()

def write_account_and_permissionsets(org, ssoadmin):
    account_permissionsets = []
    aws_accounts = get_all_aws_accounts(org)
    for account in aws_accounts:
        print(account["Name"])
        perm_sets_arn = get_permissionsets_from_account(ssoadmin, account["Id"])
        account_permissionsets.append([f"Account : {account['Name']}"])
        if not perm_sets_arn:
            account_permissionsets.append([])
            continue
        for arn in perm_sets_arn:
            perm_set_name = get_permissionsets_name(ssoadmin, arn)
            perm_set_inline = get_inline_policy(ssoadmin, arn)
            s3_inline = get_s3_permission_from_inline_policy(perm_set_inline)
            account_permissionsets.append([perm_set_name, s3_inline])
        account_permissionsets.append([])
    
    write_to_excel("permission_sets_s3_inline", account_and_permissionsets=account_permissionsets)

def main():
    sess = get_session()
    identstore = sess.client('identitystore', 'ap-southeast-1')
    # ssoadmin = sess.client("sso-admin", "ap-southeast-1")
    # org = sess.client("organizations")
    # write_account_and_permissionsets(org,ssoadmin)
    write_groups_and_members(identstore)
    # write_groups_and_members(identstore)
    # all_groups = get_all_groups(identstore)
    # contoh_group_id = all_groups[0]["GroupId"]
    # permissionsets = get_all_permisionsets(ssoadmin)
    # contoh_permissionsets = permissionsets[0]
    # cek = ssoadmin.describe_permission_set(InstanceArn=instancearn, PermissionSetArn="arn:aws:sso:::permissionSet/ssoins-8210d427f0325278/ps-65c5918b664124c0")
    # cek = ssoadmin.list_account_assignments(AccountId='948373521639', InstanceArn=instancearn, PermissionSetArn="arn:aws:sso:::permissionSet/ssoins-8210d427f0325278/ps-65c5918b664124c0")

    # perset = get_permissionsets_from_account(ssoadmin,'726231146245')
    # print(len(perset))
    # for pers in perset:
    #     cek = get_permissionsets_name(ssoadmin, pers)
    #     policy = get_inline_policy(ssoadmin, pers)
    #     perm = get_s3_permission_from_inline_policy(policy)
    #     # print(policy)
    #     print(perm)
    #     print()
    
    # print(cek)
    


    # members = get_group_members(identstore, contoh_group_id)

    return 0

if __name__ == "__main__":
    main()
