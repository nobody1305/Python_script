import boto3
import xlsxwriter
from creds import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN
identstoreid = ""

def get_session():
    return boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, aws_session_token=AWS_SESSION_TOKEN)

def get_groups(identstore):
    groups_resp = identstore.list_groups(IdentityStoreId=identstoreid)
    groups = groups_resp["Groups"]
    next_token = groups_resp.get("NextToken")
    while next_token:
        groups_resp = identstore.list_groups(IdentityStoreId=identstoreid, NextToken=next_token)
        groups += groups_resp["Groups"]
        next_token = groups_resp.get("NextToken")
    return(groups)
    # print(groups)

def get_user_in_groups(identstore, group_id):
    member_resp = identstore.list_group_memberships(IdentityStoreId=identstoreid, GroupId=group_id)
    members = member_resp['GroupMemberships']
    user_name = []
    for member in members:
        userid = member["MemberId"]["UserId"]
        user_resp = identstore.describe_user(IdentityStoreId=identstoreid, UserId=userid)
        username = user_resp["UserName"]
        user_name.append(username)
    return(user_name)

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
    all_groups = get_groups(identstore)
    groups_and_members = [("Groups", "Members")]
    i = 1
    for group in all_groups:
        print(group["DisplayName"], i)
        i+=1
        groupid = group["GroupId"]
        members = get_user_in_groups(identstore, groupid)
        for member in members:
            groups_and_members.append((group["DisplayName"], member))
    
    write_to_excel("groups_and_members_versiku", groups_and_members=groups_and_members)

def main():
    sess = get_session()
    identstore = sess.client('identitystore', 'ap-southeast-1')
    write_groups_and_members(identstore)
    # get_groups(identstore)
    # get_user_in_groups(identstore, 'f91a95bc-60d1-70ec-7127-c1c494fabce8')

if __name__ == "__main__" :
    main()