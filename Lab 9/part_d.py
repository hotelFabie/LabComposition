#Part D

#1
class User:
    def __init__(self, username : str):
        self.username = username
        
class AdminUser(User):
    def __init__(self, username : bool, ban_rights : bool = True):
        super().__init__(username)

        self.ban_rights = ban_rights

#2
admin_user = AdminUser("jevil")

#3
is_instance_1 = isinstance(admin_user, AdminUser)
is_instance_2 = isinstance(admin_user, User)
is_instance_3 = isinstance(admin_user, str)

#4
print(is_instance_1)
print(is_instance_2)
print(is_instance_3)

#5
#AdminUser is also an instance of User because it inherits (base behavior) from User. 
#There is an "is-a" relationship, and so, AdminUser is a User.