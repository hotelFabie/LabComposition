#Part H

#1 and #2
class User:
    def __init__(self, username : str, email : str):
        self.username = username
        self.email = email
        
    #3
    def change_username(self, new_username):
        if len(new_username.strip()) < 3 or len(new_username.strip()) > 16:
            raise ValueError("Username must be between 3 and 16 characters.")
        self.username = new_username

    #6
    def see_metadata(self):
        print(f"username: {self.username}, email: {self.email}")

#4
class AdminUser(User):
    #5
    def __init__(self, username : str, email : str, super_privileges : bool = False):
        super().__init__(username, email)
        self.super_privileges = super_privileges

    #6
    def see_metadata(self):
        print("this user's data is not publicly visible.")

    #4 (Own method)
    def reassign_super_privileges(self, decision : bool):
        self.super_privileges = decision

class PremiumUser(User):
    #5
    def __init__(self, username : str, email : str, tokens : int = 5):
        super().__init__(username, email)

        #9
        if tokens < 0:
            raise ValueError("Premium user cannot have below 0 tokens.")

        self.tokens = tokens

    #6 and #7
    def see_metadata(self):
        print(f"{super().see_metadata()}, premium status with {self.tokens} tokens")

    #4 (Own method)
    def update_tokens(self, new_tokens):
        if new_tokens < 0:
            raise ValueError("Premium user cannot have below 0 tokens.")

        self.tokens = new_tokens

#8
#An object each.
user = User("eien_mugen", "eien_mugen@mailbox.org")
premium_user = PremiumUser("valueadvance", "moneytowaste@gmail.com", 10)
admin_user = AdminUser("naka", "naka@admin.v8.jp", True)


user.change_username("eien_raijuu")
premium_user.change_username("advanced")

#Prints will occur within the method.
user.see_metadata()
premium_user.see_metadata()
admin_user.see_metadata()

premium_user.update_tokens(10)
print(f"Tokens: {premium_user.tokens}")

admin_user.reassign_super_privileges(False)
print(f"Admin [{admin_user.username}] right to super privileges: {admin_user.super_privileges}")

#10
#Both AdminUser and PremiumUser have an "is-a" relationship with User, because they inherit everything User has,
#proven by them both calling their superclass's - User - initialization method within their own using super().  