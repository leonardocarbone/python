import datetime

# Create a new time
ts = datetime.time(14,12,45) # or datetime.date(YEAR,MONTH,DAY)
print ts

print ts.hour
print ts.minute

print datetime.time.min # Prints the minimum time accepted
print datetime.time.max # Prints the maximum time accepted

# Create a new date
today = datetime.date.today()
print today

print today.year
print today.day

print datetime.date.min # Prints the minimum date accepted
print datetime.date.max # Prints the maximum date accepted

# Change the date
new_today = today.replace(year=1981)
print new_today

# Print the difference in days between those dates
print today-new_today
