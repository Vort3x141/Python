print("Welcome to the tip calculator.\n")
total_bil=float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
finaltip = (total_bil * tip)/100
new_bill = total_bil+finaltip
people = int(input("How many people to spilit the bill?\n"))
per_person_bill = new_bill/people
print(f"Each person should pay: ${round(per_person_bill,2)}")