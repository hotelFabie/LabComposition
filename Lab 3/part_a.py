# Part A
# -----1-----
number = 5

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# -----2-----
age = int(input("age: "))

if age <= 12:
    print("child")
elif age >= 13 and age <= 17: 
    print("teenager")
elif age >= 18 and age <= 64:
    print("adult")
else:
    print("elderly")

# -----3-----
username = "fabi"
password = "s3cr3t"

entered_username = str(input("username: "))
entered_password = str(input("password: "))

if entered_username == username and entered_password == password:
    print("[logged in]")
else:
    print("[failed login: incorrect credentials]")

# -----4-----
score = int(input("score: "))
if score >= 0 and score <= 20:
    print("grade E")
elif score > 20 and score <= 40:
    print("grade D")
elif score > 40 and score <= 60:
    print("grade C")
elif score > 60 and score <= 80:
    print("grade B")
elif score > 80 and score <= 100:
    print("grade A")
    
# -----5-----
order_total = 40
is_member = True

if order_total > 20 and is_member:
    print("shipped")
else:
    print("not shipped")

# -----6-----
# (1)
a = 1

#Predicting to be True
print(bool(a) == True)

# (2)
b = 5.5

#Predicting to be True
print(type(b) != int)

# (3)
c1 = 99
c2 = 99.9

#Predicting to be False 
print(c1 > c2)

# (4)
d1 = -1
d2 = -100

#Predicting to be False
print(d1 < d2)

# (5)
#Predicting to be True
e = 4 * 23
print(e >= 90 and e <= 100)
