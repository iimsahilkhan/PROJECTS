import random

print("Welcome to Your Passwaord Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@$&0123456789"

number = int(input("Enter Amount of Password to Generate: "))

length = int(input("Enter the Password length: "))

print("\nHere are Your Password")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)