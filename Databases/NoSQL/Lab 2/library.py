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
#   Loaned books : list with many dictionaries, with each dictionary comprising: {book_id, loan_date (datetime), return_date (datetime)}. 
#       A check consisting of two conditions. 1. Length must be 3 or more. 2. No borrow_date must give a difference of 14 days or more to today. | Inform the user.

#Comments that will not be relevant later on:
#We do not explicitly need to have these made beforehand, the functions will be able to take care of it.

#Not implementing it from the perspective of having the member login and do options, because it is not smart to store passwords in plain-text.
#In that case, an encryption algorithm would be beneficial, and then the program will become bigger.
#So, for the scope of the project, you steer the members on your own, with them only serving as a representation of what they are to be. 

#-----
from datetime import datetime as dt, timedelta
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["library"] 

def borrow_book():
    #WIP: Check on both of these...
    member_id = int(input("Which member wants to borrow? (enter id): "))
    book_id = int(input("Which book do you want to borrow? (enter id): "))

    current_member = db.members.find_one({'_id' : member_id})
    current_book = db.books.find_one({'_id' : book_id})

    loan_count = db.members.count_documents({'loaned_books' : {'_id' : member_id}})

    #Out of stock
    if current_book.get('stock') <= 0:
        print(f"Book with id {book_id} is out of stock.")
        return

    #Already loan limit
    elif loan_count >= 3:
        print(f"User with id {member_id} is currently already borrowing 3 books.")
        return
    
    #Delayed return of loaned book
    loaned_books = current_member.get('loaned_books')
    if len(loaned_books) > 0:
        for book in loaned_books:
            if book['return_date'] - dt.now() < timedelta(0):    
                print(f"Cannot borrow another book before your books currently borrowed past the expected return date has been given back.")
                return
        
    #This does not target anything.
    #We need to do a $set here.    
    db.members.update_one(
        {'_id': member_id}, 
        {'$push': 
            {
            'loaned_books': 
                {
                    'book_id': book_id, 
                    'loan_date': dt.now(), 
                    'return_date': dt.now() + timedelta(days=14)
                }
            }
        }
    )

    db.books.update_one({'_id' : book_id}, {"$inc" : {'stock' : -1}})   


def return_book():
    member_id = int(input("Which member wants to return? (enter id): "))

def search_book():
    pass

def show_member_status():
    member_id = int(input("Which member? (enter id): "))

def register_new_member():
    #Checks will be applied so that unexpected values aren't passed.
    first_name = input("First name: ").strip().capitalize()
    last_name = input("Last name: ").strip().capitalize()
    email = input("Email: ").strip()
    
    #The _id should not have to be written.
    #The 'loaned_books' should work like tags has done before.
    #The loaned books MAY be a dictionary instead.
    db.members.insert_one({"first_name" : first_name, "last_name" : last_name, "email" : email, "loaned_books" : []})

def menu():
    print("1. Borrow book. 2. Return book. 3. Search for books 4. Show member status, 5. Register new member 0. Quit")

def start():
    while True:
        menu()
        
        option = int(input(">"))
        match option:
            case 1:
                borrow_book()
            case 2:
                return_book()
            case 3:
                search_book()
            case 4:
                show_member_status()
            case 5:
                register_new_member()
            case 0: 
                print("Quitting...")
                break
            case _:
                print("Not a valid input.")

#-----
start()