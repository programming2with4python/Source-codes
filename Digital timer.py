# Import the time module
import time

# Define a function to display the timer
def display_timer(seconds):
    # Convert seconds to hours, minutes and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    # Format the timer as hh:mm:ss
    timer = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    # Print the timer
    print(timer, end="\r")

# Ask the user to enter the duration of the timer in seconds
duration = int(input("Enter the duration of the timer in seconds: "))

# Loop from the duration to zero, decrementing by one each second
for i in range(duration, -1, -1):
    # Display the timer
    display_timer(i)
    # Wait for one second
    time.sleep(1)

# Print a message when the timer is done
print("Time's up!")
