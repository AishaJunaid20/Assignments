import math
import datetime
import calendar

# Math functions
print("Square root of 16 is:", math.sqrt(16))
print("5 raised to power 3 is:", math.pow(5, 3))

# Date & time
today = datetime.date.today()
print("Today's date is:", today)

# Calendar for a month
year = 2025
month = 4
print(f"\nCalendar for {month}/{year}:\n")
print(calendar.month(year, month))
