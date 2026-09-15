#Part D

# -----1-----
def show_profile(**info):
    for key, value in info.items():
        print(f"key: {key}, value: {value}")

profile = {"name": "john", "age" : 38, "work" : "construction worker"}

#Proof for myself
show_profile(**profile)

# -----2-----
def create_user(username, **details):
    user = {"username" : username}
    for key, value in details.items():
        user[key] = value

    return user

details = {"age": 22, "country" : "Sweden", "tall" : False}

#Proof for myself
print(create_user("fabi83", **details))

# -----3-----
def build_product(name, price, **metadata):
    product = {"name" : name, "price" : price}
    for key, value in metadata.items():
        product[key] = value

    return product

#Proof for myself
metadata = {"weight" : "50kg", "waterproof" : False, "color" : "beige"}
print(build_product("Cardboard Helicopter", 159.99, **metadata))

# -----4-----
def get_valid_settings(**settings):
    valid_settings = {}
    for key, item in settings.items():
        if item != None:
            valid_settings[key] = item

    return valid_settings

#Proof for myself
settings = {"colorSelected" : None, "fontPreference" : "IBM Mono Sans", "homeReturnDefault" : "Crtl+Alt+H", "fontSizePreference" : None}
print(get_valid_settings(**settings))

# -----5-----
#normal named parameter function using **dictionary unpacking
def print_person(name, age, occupation):
    print(f"{name} - {age} years old - works with {occupation}")

person = {"name" : "Fabi", "age" : 22, "occupation" : "programming."}

#Proof for myself
print_person(**person)