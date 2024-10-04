# Ask for the user's name
name = input("Enter your name: ")

# Print a greeting
print(f"Hello, {name}! My name is Potemkin and I'm a bot :) .")

# Variables for storing personal info
username = "albionLives"
followers = 1500
recent_tweet = "England for English"

# Print Twitter-related info
print(f"Username: {username}")
print(f"Followers: {followers}")
print(f"Recent Tweet: {recent_tweet}")

# Variables for storing other personal info
subject_name = "John Doe"
dob = "1990-01-01"

# Print out the information
print("Subject Name:", subject_name)
print("Date of Birth:", dob)


import random
import string

def generate_password(length):
    # Create a pool of characters (letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to create the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask the user for desired password length
length = int(input("Enter the desired password length: "))
print(f"Your generated password is: {generate_password(length)}")