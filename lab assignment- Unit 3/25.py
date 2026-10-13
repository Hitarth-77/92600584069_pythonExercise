from datetime import date, datetime

today = date.today()
now = datetime.now()

print("Current date:", today)
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)