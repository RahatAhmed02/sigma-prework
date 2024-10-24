import datetime
from dateutil.relativedelta import relativedelta

print("""This program calculates the difference in years between today and the date you enter.
Please enter the year, month, and day when prompted.""")

while True:
    try:

        user_date_input_year = int(input("Enter the year (YYYY): "))
        user_date_input_month = int(input("Enter the month (1-12): "))
        user_date_input_day = int(input("Enter the day (1-31): "))

        formatted_user_date = datetime.date(
            user_date_input_year, user_date_input_month, user_date_input_day)

        today = datetime.date.today()

        if formatted_user_date > today:
            print("The date you entered is in the future. Please enter a past date.")
            continue

        age_difference = relativedelta(today, formatted_user_date)
        age_years = age_difference.years

        print(f"It has been {age_years} years.")
        break

    except ValueError:
        print("Invalid input. Please enter numeric values for year, month, and day.")
