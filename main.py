# main.py

# Check String

# Prompt the user to enter their username
name = input("Enter your username: ")

# Download bad-words list
# !wget https://www.cs.cmu.edu/~biglou/resources/bad-words.txt

# Open and read the bad-words list from a file
with open("bad-words.txt") as f:
    bad_words = f.read().splitlines()

# Check if the username contains any bad words
for word in bad_words:
    if word in name:
        print("Bad username :/, try again")
        # Prompt the user to enter a new username if a bad word is found
        name = input("Enter your name: ")
        break

# Welcome the user if the username is acceptable
print("\nWelcome", name)
exit()
# This line will not be executed due to the exit() above
print("Good username")
