import json
from datetime import datetime

# Load expenses from file (if it exists)
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Travel): ")
    date = datetime.now().strftime("%Y-%m-%d")
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added!")

# View expenses by category
def view_expenses(expenses):
    category = input("Enter category to filter (or press Enter for all): ")
    total = 0
    print("\nExpenses:")
    for expense in expenses:
        if not category or expense["category"].lower() == category.lower():
            print(f"{expense['date']} - {expense['category']}: ${expense['amount']}")
            total += expense["amount"]
    print(f"Total: ${total:.2f}")

# Main program
def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()