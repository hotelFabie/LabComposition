#Part H

#1 and #2
class User:
    def __init__(self, username : str, email : str):
        self.username = username
        self.email = email
        
    #3
    #WIPPY...

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

class PremiumUser(User):
    #5
    def __init__(self, username : str, email : str, tokens : int = 5):
        super().__init__(username, email)
        self.tokens = tokens

    #6 and #7
    def see_metadata(self):
        return super().see_metadata() + f", premium status with {self.tokens} tokens"



#10