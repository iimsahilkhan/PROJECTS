# Import the time module for sleep functionality
import time

def countdown(t):
    """
    Function to create a countdown timer that displays minutes and seconds.
    
    Args:
        t (int): Total time in seconds for the countdown
    """
    while t:
        # Convert seconds to minutes and seconds 
        mins, secs = divmod(t, 60)  
        # Format the time as MM:SS
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        # Print the timer and return to the start of the line
        print(timer, end="\r")
        # Wait for 1 second
        time.sleep(1)
        # Decrease the time by 1 second
        t -= 1

    # Print completion message when timer ends
    print('Timer Completed')

# Get user input for timer duration in seconds
t = input("Enter the time in Second: ")
# Start the countdown with the user input
countdown(int(t))