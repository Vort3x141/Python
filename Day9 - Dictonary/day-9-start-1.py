programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#Retriving items from dictionary
# print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loops"] = "The action of doing something over and over again."


#Create an empty dictionary.
empty_dictionary = {}


#Wipe an existion dictionary.
# programming_dictionary = {}
# print(programming_dictionary)


#Edit an itam in a dictionary
# programming_dictionary["Bug"] = "An moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
