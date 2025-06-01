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
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!\n")
            else:
                print(f"\nReminder: '{task}' is a high priority task. Try to do it as soon as possible.\n")

        case "medium":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a medium priority task that should be done today.\n")
            else:
                print(f"\nReminder: '{task}' is a medium priority task. Fit it into your schedule.\n")

        case "low":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a low priority task that still needs to be done today.\n")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.\n")

        case _:
            print("\nInvalid priority entered. Please enter 'high', 'medium', or 'low'.\n")

    # Ask user if they want to add another task (optional)
    another = input("Do you want to enter another task? (yes/no): ").lower()
    if another != "yes":
        print("\nGoodbye! Stay productive!")
        break
