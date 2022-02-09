import random

name = input("Give me everybody's names, seperated by a comma. ")

names = name.split(", ")

count_name = len(names)


random_int = random.randint(0, count_name-1)

random_name = random_int

print(f"{names[random_name]} is going to buy the meal today!")
