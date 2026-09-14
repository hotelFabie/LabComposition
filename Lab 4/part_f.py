# Part F

# -----1-----
#Not sure what defines "normalize" here beyond giving everybody the same conditions.
def normalize_name(name) -> str:
    return name.upper().strip()



#WIP: Adhere to Aladdin's explanation later on.
def validate_age(age) -> bool:
    if age >= 18 and age <= 35:
        return True
    else: 
        return False

def calculate_reg_fee(age, status) -> int | float:
    fee = 300
    if age < 25:
        fee *= 0.9
    if status == 'student':
        fee *= 0.85
    return fee


def create_participant_dictionary(name : str, age : int, status : str): 
    if validate_age(age):
        return {"name" : name, "age" : age, "status" : status}
    else:
        return None

# -----2-----
p_1 = create_participant_dictionary("Jason", 18, 'student')
p_2 = create_participant_dictionary("Kira", 21, 'worker')
p_3 = create_participant_dictionary("Ishmael", 26, 'student')
p_4 = create_participant_dictionary("Samuel", 19, 'neet')
p_5 = create_participant_dictionary("Edwin", 23, 'student')
p_6 = create_participant_dictionary("Skylar", 18, 'worker')
p_7 = create_participant_dictionary("Nirvana", 25, 'worker')
p_8 = create_participant_dictionary("Monica", 24, 'neet')

participants = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8]

# -----3-----
def calculate_total_reg_fee(participants: list) -> int | float: 
    total_fee = 0
    for participant in participants:
        sub_fee = calculate_reg_fee(participant['age'], participant['status'])
        total_fee += sub_fee

    return total_fee

#Just proof that something happens
print(calculate_total_reg_fee(participants))

# -----4-----
def get_students(participants: list):
    students = []
    for participant in participants:
        if participant['status'] == 'student':
            students.append(participant)
    return students

#Proof for myself
print(get_students(participants))

# -----5-----
def get_oldest_participant(participants : list):
    #Must have something to compare to, first. 
    oldest = participants[0]
    for participant in participants:
        if participant["age"] > oldest["age"]:
            oldest = participant
    return oldest

#Proof for myself
print(get_oldest_participant(participants))

# -----6-----
def summarize_participant(participant) -> str:
    #take everything as a string
    return f"{participant['name']} is {participant['age']} years old, and is currently a {participant['status']}."

#Proof for myself
print(summarize_participant(participants[3]))

# -----7-----
#This is not really a question, I guess, but rather just a step describing everything above.