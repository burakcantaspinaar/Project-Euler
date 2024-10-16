months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week_index = 0
sunday_count = 0

for year in range(1900, 2001):
    for month, days_in_month in months.items():
        if month == "February" and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            days_in_month = 29

        if year >= 1901 and weekdays[week_index] == "Sunday":
            sunday_count += 1

        week_index = (week_index + days_in_month) % 7

print("Total number of months where the 1st is a Sunday:", sunday_count)
