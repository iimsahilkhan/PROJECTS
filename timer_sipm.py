import time  # This module provides various functions to manipulate time values

def countdown(seconds):
    while seconds > 0:
        # Calculate minutes and remaining seconds
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        
        # Show the time in MM:SS format
        time_display = f"{minutes:02d}:{remaining_seconds:02d}"
        print(time_display, end="\r")
        
        # Wait for 1 second
        time.sleep(1)
        
        seconds -= 1  # Count down by 1 second

    # Show message when timer is done
    print("Time's up!")

# Ask user how long they want the timer to run
timer = input("How many seconds should the timer run?: ")
countdown(int(timer))