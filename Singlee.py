#This class violates the single-responsibility 
class UserManager:
    def __init__(self, user_data): 
        self.user_data = user_data
    
    def create_user(self, name, age):
        self.user_data[name] = age
    
    def delete_user(self, name):
        del self.user_data[name]
    
    def save_to_database(self):
        with open("users.txt", "w") as file:
            for name, age in self.user_data.items():
                file.write(f"{name},{age}\n")
    
    def send_welcome_email(self, name):
        print(f"Sending welcome email to {name}")


user_data = {}
a = UserManager(user_data)
a.create_user('menna', 20)


# This class not violates the single-responsibility
 

class UserManager:
    def __init__(self, user_data): 
        self.user_data = user_data
    
    def create_user(self, name, age):
        self.user_data[name] = age
    
    def delete_user(self, name):
        del self.user_data[name]
        
class DataBase:
    def __init__(self,user_data):
        self.user_data = user_data
        
    def save_to_database(self):
         with open("users.txt", "w") as file:
             for name, age in self.user_data.items():
                 file.write(f"{name},{age}\n")

class Email:
   
    def send_welcome_email(self, name):
        print(f"Sending welcome email to {name}")
        
    











