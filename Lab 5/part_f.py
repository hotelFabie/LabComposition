#Part F

#As discussed with a teacher, validation for types of sections or metadata wasn't required.
#Went with strings for each section.
# -----1, 2 & 3-----
#These basically go together, as not all of these are an implementation step, I notice.
def create_report(title, *sections, **metadata):
    report = {"title" : title, "sections" : []}

    for section in sections:
        report["sections"].append(section)

    #could be nice to do a check here of things that really are allowed to belong in here.
    for key, value in metadata.items():
        report[key] = value

    return report

# -----4-----
#Nothing specified beyond multi-line string
def summarize_report(report):
    summary = "--SUMMARY ABOUT THE PROVIDED REPORT--"
    for key, value in report.items():
        summary += f"\n{key} : {value}."
    return summary

report = create_report("world disaster", "start of ages", "destruction", "possible light in the tunnel", author="jason yang", department="predictive sciences", version=1, confidential=True, date="21/09/2025")

print(summarize_report(report))

# -----5-----
def count_words(*sections):
    count = 0
    
    for section in sections:
        words = section.split(" ")
        for word in words:
            count += 1

    return count

print(count_words(report["sections"]))

# -----6-----
#here the prefined data can be done, and that i am already familiar with.