
# Part 1: Display the Current Date and Time
from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    # Format: "YYYY-MM-DD HH:MM:SS" for 12hrs use %I, for am/pm use %p for CST timezone, %Z, UTC offset %z
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)
    return formatted_date
      
display_current_datetime()


# Part 2: Calculate a Future Date

days_inputed = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_inputed)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print('future date:', formatted_future_date)
    return formatted_future_date

calculate_future_date()