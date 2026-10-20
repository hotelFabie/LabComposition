#Doing most things somewhat or entirely externally.
#Just using this as further documentation of what I have done.

#1
#Storing and creating this in a private/outside resource.

#2
#Added to the top of main.py in part 1 & 2.

#3
#If API_KEY is missing in .env, it will be equal to None.
#The check_key-function always checks the case of the parameter x_api_key's argument not being to whatever API_KEY is.
#Since a string will never be equal to None, this check will succeed, and it will throw the HTTPException.

#4