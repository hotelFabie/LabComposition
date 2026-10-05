#Part F

#1
class Notification:
    def __init__(self):
        pass

    def send(self) -> str:
        return "Notification sent."

#2
class EmailNotification(Notification):
    def __init__(self):
        super().__init__()

    #3
    def send(self) -> str:
        return "Email sent."

class SMSNotification(Notification):
    def __init__(self):
        super().__init__()

    #3
    def send(self) -> str:
        return "SMS sent."

#4
notification = Notification()
email_notification = EmailNotification()
sms_notification = SMSNotification()

print(notification.send())
print(email_notification.send())
print(sms_notification.send())

#5
#In the first case, the superclass's method is being run, 
#and in the other two (subclass instances), their own variants of the method are called.