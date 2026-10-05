#Part A

#1 and #2
class EmailNotification():
    def __init__(self):
        pass

    def send() -> str:
        return "Email!"

class SMSNotification():
    def __init__(self):
        pass

    def send() -> str:
        return "SMS!"

class PushNotification():
    def __init__(self):
        pass

    def send() -> str:
        return "Push!"

#3
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
]

#4
for notification in notifications:
    notification.send()

#5
#Python sort of acts by looking at the object rather than explicitly on the class,
#and since all of them have a method with the same name, it simply just takes each type of object and applies the method belonging to them.