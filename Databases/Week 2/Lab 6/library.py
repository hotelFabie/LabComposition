#[Design decisions]

#-First of all, the structure of both collections for readability when implementing.
#Book:
#   _id: integer (PRIMARY KEY)
#   Title : string/text 
#   Author: string/text
#   Genres: list of string/text
#   Stock: integer  
#       A check must be done that this never goes below 0. | Inform the user.
#   Reviews: a list of dictionaries with the structure: {'member_id' (Not to be UNIQUE; should a member not be able to read and give a second opinion?), 'rating', 'review_text'}

#Member:
#   _id: integer (PRIMARY KEY)
#   First name: string/text
#   Last name: string/text
#   Mail: string/text (UNIQUE),
#   Borrows : dictionary comprised of {book_id, borrow_date (datetime)}. 
#       A check consisting of two conditions. 1. Length must be 3 or more. 2. No borrow_date must give a difference of 14 days or more to today. | Inform the user.

#We do not explicitly need to have these made beforehand, the functions will be able to take care of it.

#Not implementing it from the perspective of having the member login and do options, because it is not smart to store passwords in plain-text.
#In that case, an encryption algorithm would be beneficial, and then the program will become bigger.
#So, for the scope of the project, you steer the members on your own, with them only serving as a representation of what they are to be. 

def borrow_book():
    member_id = input("Which member wants to borrow? (enter id)")
    #Requires a check on the member.
    #Technically, books could have the same name, but you rarely get intrigued by a book based off of the ISBN nor an ambiguous, so it will limited to...

def menu():
    print("1. Borrow book. 2. Return book. 3. ")

def start():
    #input asking for who the member is to be. 
    while True:
        menu()
        
        option = input()
        match option:

            case 1:
                borrow_book()
            case 2:

            case 3:
