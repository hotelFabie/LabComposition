#Part F

#As discussed with a teacher, validation for types of sections or metadata wasn't required.
#Went with strings for each section.

# -----1, 2 & 3-----
#These basically go together, as not all of these are an implementation step, I notice.
def create_report(title, *sections, **metadata):

    #For question 7
    expected_metadata = ["author", "department", "version", "confidential", "date"]
    
    report = {"title" : title, "sections" : []}

    for section in sections:
        report["sections"].append(section)

    for key, value in metadata.items():
        report[key] = value
        if key in expected_metadata:
            expected_metadata.remove(key)

    #For question 7
    if len(expected_metadata) > 0:
        print(f"metadata not provided: {expected_metadata}")

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
    total = 0

    for section in sections:
        total += len(section.split())
    
    return total

#Proof for myself.
print(count_words(*report["sections"]))

# -----6-----
metadata_one = {"author" : "adolf silfver", "department" : "nordic linguistics", "version" : 3, "confidential" : True, "date" : "06/01/2011"}
metadata_two = {"author" : "rob kaufmann", "department" : "paganism", "version" : 1, "confidential" : False, "date" : "15/09/2026"}

#Proof for myself.
print(create_report("a synopsis of the north germanic tribes' languages", "proto-traits", "extinct branches, and their barriers" "unique case: icelandic", **metadata_one))
print(create_report("the one true religious answer: paganism", "dominant truth", "response against hate", "why you're wrong", **metadata_two))

# -----7-----
print(create_report("all about letters", "a", "b", confidential=False))
#All the metadata that is not inserted - but implicitly expected - get printed out as a side effect of the function.