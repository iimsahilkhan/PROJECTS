balance = 0  # Initialize global balance

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount < 0:
        print("This is not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    global balance
    amount = float(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

is_running = True

while is_running:
    print("\nBANKING PROGRAM BY MANAV SAXENA")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice")

print("Thank you! Have a nice day!")