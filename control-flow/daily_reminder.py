# daily_reminder.py

while True:
    # Prompt for user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task based on priority using match-case
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Try to do it as soon as possible.")

        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be done today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Fit it into your schedule.")

        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that still needs to be done today.")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")

        case _:
            print("Invalid priority entered. Please enter 'high', 'medium', or 'low'.")
    break 
    # end everything,flow complete
    # Uncomment the following lines if you want to allow the user to add multiple tasks


    # Ask user if they want to add another task (optional)
    # another = input("Do you want to enter another task? (yes/no): ").lower()
    # if another != "yes":
    #     print("\nGoodbye! Stay productive!")
    #     break

# # daily_reminder.py

# # Prompt user for task details
# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# # Initialize reminder message
# reminder = f"Reminder: '{task}' is a {priority} priority task"

# # Process priority using match case
# match priority:
#     case "high":
#         reminder += " that should be tackled soon"
#     case "medium":
#         reminder += " that you should plan to complete"
#     case "low":
#         reminder += ". Consider completing it when you have free time"
#     case _:
#         reminder = f"Reminder: '{task}' has an invalid priority. Please use high, medium, or low"

# # Adjust reminder for time sensitivity
# if time_bound == "yes":
#     reminder += " that requires immediate attention today!"
# elif time_bound == "no" and priority in ["high", "medium", "low"]:
#     reminder += "."
# else:
#     reminder = f"Reminder: '{task}' has invalid time-bound input. Please use yes or no."

# # Output the customized reminder
# print(reminder)