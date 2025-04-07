import random
import string

print("Welcome to Your Passwaord Generator")

char_val = string.ascii_letters + string.punctuation + string.digits

number = int(input("Enter Amount of Password to Generate: "))

length = int(input("Enter the Password length: "))

print("\nHere are Your Password")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(char_val)
    print(password)