# Part G
# -----1-----
study_sessions = [
    {"subject" : "math", "minutes" : 30},
    {"subject" : "chemistry", "minutes" : 45},
    {"subject" : "python", "minutes" : 15},
    {"subject" : "math", "minutes" : 60},
    {"subject" : "academic writing", "minutes" : 50},
    {"subject" : "c++", "minutes" : 50},
    {"subject" : "chemistry", "minutes" : 15},
    {"subject" : "chemistry", "minutes" : 45},
    {"subject" : "python", "minutes" : 30},
    {"subject" : "microprocessors", "minutes" : 60},
]

# -----2-----
total_minutes = 0

for session in study_sessions:
    total_minutes += session["minutes"]

print(total_minutes)

# -----3-----
minutes_per_subject = dict()

for session in study_sessions:
    minutes_per_subject[session["subject"]] = minutes_per_subject.get("subject", 0) + session["minutes"]

print(minutes_per_subject)

# -----4-----
longest_session = study_sessions[0]

for session in study_sessions:
    if session["minutes"] > longest_session["minutes"]:
        longest_session = session

#Identifying it by printing:
print(f"Longest session is {longest_session['minutes']} minutes, with the subject being {longest_session['subject']}.")

# -----5-----
for session in study_sessions:
    if session["minutes"] > 45:
        print(session)

# -----6-----
menu = "=== commands: [sessions], [time], [subject], [quit] ==="

while True:
    print(menu)
    command = str(input(">"))
    if command == "quit":
        break
    elif command == "sessions":
        for index, session in enumerate(study_sessions):
            print(f"[{index + 1}] {session['subject']} for {session}")         
    elif command == "time":
        total_time = 0
        for session in study_sessions:
            total_time += session["minutes"]
        print(f"total time: {total_time} minutes")
    elif command == "subject":
        subject = str(input("subject>"))
        if not subject:
            print(f"{subject} was not found")
            break
        for session in study_sessions:
            if session["subject"] == subject:
                print(f"{session['subject']} - {session['minutes']} min")
    else:
        print("error. write an available command.")

# -----7-----
#Sort of already implemented it where it was necessary in 6.