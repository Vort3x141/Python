# def greet():
#     print("Hello")
#     print("How do you do ?")
#     print("Isn't the weather nice today?")

# greet()




#Function that allows for input

# def greet_with_name(name): #name = parameter
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Vinayak") #Vinayak = argument




#FUnctions with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Vinayak","Meerut") # Position Argument






#Functions with keyword arguments

def greet_with_keyargs(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with_keyargs(location = "Meerut", name = "Vinayak")


