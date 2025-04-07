# Python command-line based "LOVE CALCULATOR"
import random

def calculate_love():
	st = '0123456789'
	digit = 2  # We want a 2-digit number for the percentage
	return "".join(random.sample(st, digit)) #Generate a random 2-digit number by sampling from the digits

print("Love Calculator - How much is he/she into you")
print("--------------------------------------------")

name1 = input("Enter Your Name: ")
name2 = input("Enter Your Partner Name: ")

love_percentage = calculate_love()  # Calculate the love percentage

# Display the result with both names and the calculated percentage
print(f"\nLove Percentage between {name1} and {name2}: {love_percentage}%")