def prime_checker(number):
    flag = True
    for i in range(2,number):
        if number % i == 0:
            flag = False
        else:
            flag = True
    if flag:
        print("Its a prime number.")
    else:
        print("Its not a prime number.") 

n = int(input("Check this number: "))
prime_checker(number=n)
