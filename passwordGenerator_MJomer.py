#Imports the modules for the specific action
import random
import string

try:
    #This here asks the user to enter any length of their choice
    length = int(input("Enter a length of your choice: "))

    #This concatenates all characters 
    characters = string.ascii_letters
    characters += string.digits
    characters += string.punctuation


    password = ""

    #This uses a loop to generate the password
    for i in range(length):
        #This randomizes characters 
        password += random.choice(characters)
    #This establishes the final product of the generated given password
    print(password)
#This indicates alphabets or special characters as an error
except ValueError:
    print("No alphabets or special characters are allowed. Please type in a number.")