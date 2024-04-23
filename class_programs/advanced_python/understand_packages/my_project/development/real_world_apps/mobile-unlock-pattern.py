# WAP to unlock the mobile device using a pattern
"""
User enters a correct password in 5 attempts, phone will be unlocked.
If a user enters an incorrect password for 5 attempts,
You have to wait for 30 seconds to try again.
This process repeats
"""
import time

lock_pattern = 12345
i = 1
while i <= 5:
    pattern = int(input("Enter the unlock pattern "))
    if pattern == lock_pattern:
        print("Mobile is successfully unlocked")
        break
    print("Wrong pattern")

    if i == 5:
        print(f"you have incorrectly drawn your unlock pattern {i} times. Try again in 30 seconds")
        time.sleep(30)  # Waiting for 30 seconds
        i = 1
        continue

    i = i + 1

print("End of the program")
