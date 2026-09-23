#Part A

#1
class BadTeam:
    def __init__(self, name : str, members : list[str] = []):

        self.name = name
        self.members = members

    def add_member(self, member : str):
        self.members.append(member)
        
#2
bt1 = BadTeam("Evil Peeble")
bt2 = BadTeam("Mahi T2")

bt1.add_member("Madison")

print(bt1.members)
print(bt2.members)

#They will have the same members, because a default parameter being of a reference type will point to the same collection/[part in memory].

#3
class Team:
    def __init__(self, name : str, members : list[str] = None):
        self.name = name

        if members == None: 
            members = []

        self.members = members

    def add_member(self, member : str):
        self.members.append(member)

#4
t1 = Team("Evil Peeble")
t2 = Team("Mahi T2")

t1.add_member("Madison")

print(t1.members)
print(t2.members)

#When printed, it will show that t1 and t2 have separate member lists, as Madison is not added to t2.