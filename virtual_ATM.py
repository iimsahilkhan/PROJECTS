print("\n Welcome to the Virtual ATM\n")

balance = 0
pin = int(input("Set your 4-digit PIN: "))
print("\n PIN Set Successfully! Please remember it.\n")

while True:
    entered_pin = int(input("For Access Banking Features, Enter your PIN: "))
    if entered_pin != pin:
        print("Incorrect PIN! Access Denied")
        continue

    print("\nChoose an Option:")
    print("1 -> Check Balance")
    print("2 -> Withdraw Money")
    print("3 -> Deposit Money")
    print("4 -> Change PIN")
    print("5 -> Exit")

    choice = int(input("Enter Your Choice (1-5): "))

    if choice == 1:
        print(f"Your Current Balance is Rs.{balance}")

    elif choice == 2:
        entered_pin = int(input("Enter PIN to Withdraw: "))
        if entered_pin != pin:
            print("Incorrect PIN! Access Denied")
            continue
        amount = int(input("Enter Amount to Withdraw: "))
        if amount > balance:
            print("Insuficiant Balance! Withdraw Failled")
        else:
            balance -= amount
            print(f"Withdraw Succesful! Remaining Balance: Rs.{balance}")

    elif choice == 3:
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin != pin:
            print("Incorrect PIN! Access Denied")
            continue
        amount = int(input("Enter Amount to Deposit: "))
        balance += amount
        print(f"Deposit Successful! New Balance: Rs.{balance}")

    elif choice == 4:
        entered_pin = int(input("Enter Your PIN: "))
        if entered_pin != pin:
            print("Incorrect PIN! Access DEenied")
            continue
        pin = int(input("Enter New PIN: "))
        print("PIN Changed Successfully")

    elif choice == 5:
        print("Thank You for using Virual ATM\nGood Bye")
        break
    else:
        print("Invalid Choice , Please enter a Number Between (1-5)")   