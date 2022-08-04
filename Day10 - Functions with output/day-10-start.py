#Functions with Outputs

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input."

    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"
    #nothing will be executed after return :)
    
        
print(format_name(input("Whats is your first name?"), input("What is your last name ?")))
