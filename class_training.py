import user
import post_class

app_user1 = user.User("email@com", "Faizal", "pass", "Devops Engineer")
app_user2 = user.User("mail@com", "rina", "pass", "Seller")
# app_user1.get_user_info()
# app_user1.change_job_title("Head DevOps")
# app_user1.get_user_info()


new_post = post_class.Post("on secret mission today", app_user1.name)
new_post.get_post_info()