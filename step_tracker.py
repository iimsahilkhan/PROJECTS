import datetime
import json
import os

DATA_FILE = "step_data.json"

# Load step data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save step data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Get today's date string
def get_today():
    return str(datetime.date.today())

# Add steps
def add_steps(data, steps):
    today = get_today()
    data[today] = data.get(today, 0) + steps
    print(f"{steps} steps added. Total today: {data[today]} steps.")

# View steps
def view_steps(data):
    today = get_today()
    steps = data.get(today, 0)
    print(f"Steps for {today}: {steps}")

# Reset today's steps
def reset_today(data):
    today = get_today()
    data[today] = 0
    print(f"Steps reset for {today}.")

# Main program
def main():
    data = load_data()

    while True:
        print("\n--- Step Tracker ---")
        print("1. Add Steps")
        print("2. View Today's Steps")
        print("3. Reset Today's Steps")
        print("4. View All History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            try:
                steps = int(input("Enter steps to add: "))
                if steps > 0:
                    add_steps(data, steps)
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            view_steps(data)
        elif choice == "3":
            reset_today(data)
        elif choice == "4":
            for date, steps in sorted(data.items()):
                print(f"{date}: {steps} steps")
        elif choice == "5":
            save_data(data)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()


'''Would you like a GUI version using Tkinter?
Or maybe one that works with your phone’s motion sensors 
(if you're using Android + Python with sensors)?'''