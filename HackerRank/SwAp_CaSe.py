def swap_case(user_str):
    newstring = ""
    for char in user_str:
        if (char.isupper()==True):            
            newstring += char.lower()
        elif (char.islower()==True):
             newstring +=char.upper()
        else:
            newstring += char
    s = newstring
    return newstring


s = input()
result = swap_case(s)
print(result)