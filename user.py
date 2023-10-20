class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. you can contact {self.email}")

# app_user1 = User("email@com", "Faizal", "pass", "Devops Engineer")
# app_user1.get_user_info()
# app_user1.change_job_title("Head DevOps")
# app_user1.get_user_info()
# app_user2 = User("mail@com", "rina", "pass", "Seller")
# app_user2.get_user_info()