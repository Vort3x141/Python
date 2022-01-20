from calendar import month


age = int(input("Enter your age ?\n"))
max_age = 90
year_left = max_age - age
days = year_left*365
weeks = year_left*52
months = year_left*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.\n")
