# Part C
# -----1-----
courses = ["Introduction to Integrals", "Discrete Mathematics", "Introduction to Integrals", "Agentic Coding", "Introduction to Integrals", "Discrete Mathematics"]

course_set = set(courses)

print(f"List length: {len(courses)}")
print(f"Set length: {len(course_set)}")
#List length: 6, Set length: 3

# -----2-----
dev_one_skills = {"Docker", "Software Testing", "Go", "Python"}

dev_two_skills = {"Python", "Docker", "Kubernetes", "Machine Learning"}

#Union - Shared skills
print(dev_one_skills & dev_two_skills)

#Difference - Skills only developer one has
print(dev_one_skills - dev_two_skills)

#Intersection - All skills
print(dev_one_skills | dev_two_skills)

# -----3-----
character_set = {"Mario", "Kirby", "Link", "Samus"}

#Add
character_set.add("Inkling Girl")
print(character_set)

#Remove
character_set.remove("Mario")
print(character_set)

#Discard
character_set.discard("Link")
print(character_set)

#Membership testing
is_member = "Kirby" in character_set
print(is_member)

# -----4-----

#If you want to write down all possible countries you want to travel to, 
#you might say the same country again, and there is no point in saving it twice,
#so you use a set to just enter whatever countries you can brainstorm, and then check everything 
#UNIQUE you entered.