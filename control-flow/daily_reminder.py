#!/usr/bin/python3
# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and generate reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority"

# Add time sensitivity note
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    else:
        reminder += ", but it's time-bound. Consider scheduling it."
elif time_bound == "no":
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Plan time for it today."

# Print final reminder
print("\n" + reminder)

# Celebration message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")