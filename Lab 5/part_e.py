#Part E

# -----1-----
def log_event(event_type, *messages, **metadata):
    event = {"type" : event_type, "messages" : []}

    for message in messages:
        event["messages"].append(message)

    for key, value in metadata.items():
        event[key] = value

    return event

#Proof for myself
metadata = {"impact_field" : 30, "main_chemical" : "sulfur mustard"}
print(log_event("explosion", "bang!", "pow!", **metadata))

# -----2-----
#Assuming the customer should have some sort of relevancy, so I put them together as the order after processing.
def calculate_order(customer, *prices, **options):
    order = {"customer" : customer}
    total = 0

    for price in prices:
        total += price

    for key, value in options.items():
        if key == "discount":
            total *= (1 - value)
        if key == "shipping_fee" and value == True:
            total += 300

    order["total"] = total 

    return order

#Proof for myself - (Didn't prepare the metadata beforehand here as a variable.)
print(calculate_order("fabimbim", 300, 400, 500, discount=0.10, shipping_fee=True))

# -----3-----
def get_area(height, width):
    return height * width
#Understood what parameters are expected, and does the expected calculation.

def get_area(**measurements):
    return measurements[0] * measurements[1]
#Not clear what measurements, in which order, how many. Removes simplicity immensely.

# -----4-----
#Not crazily formatted, more to just see how it can receive different information.
def summarize_author(author_name, *books, **miscellaneous):
    print("---AUTHOR DATA---")
    print(f"name: {author_name}\nbooks: {books}\nmiscellaneous: {miscellaneous}")

summarize_author("haruki murakami", "norwegian wood", "1q84", age=77)
summarize_author("kazuo ishiguro", "a pale view of hills", age=71, birth_city="nagasaki", nationality="british")
summarize_author("ruth ozeki", "my year of meats", "all over creation", age=70, nationality="american")