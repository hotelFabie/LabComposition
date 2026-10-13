#[Design decisions]

#-First of all, the structure of both collections for readability when implementing.
#Book:
#   _id: integer (PRIMARY KEY)
#   Title : string/text 
#   Author: string/text
#   Genres: list of string/text
#   Stock: integer  
#       A check must be done that this never goes below 0. | Inform the user.

#Member:
#   _id: integer (PRIMARY KEY)
#   First name: string/text
#   Last name: string/text
#   Mail: string/text (UNIQUE),
#   Borrows : dictionary comprised of {book_id, borrow_date (datetime)}. 
#       A check consisting of two conditions. 1. Length must be 3 or more. 2. No borrow_date must give a difference of 14 days or more to today. | Inform the user.

#Review:
#A reason this should be its own collection is that it is its own thing separate from a book and a member, 
# but it could technically belong to both of them.



def menu():


while True:
    menu()

