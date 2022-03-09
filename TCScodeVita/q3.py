#prime numbers can be expressed as sum of other consecutive prime numbers.
#N = 20 Primes = 2,3,5,7,11,17,19




N = int(input()) 
primes = []
count = 0

for number in range (2, N+1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
              primes.append(number)
print(primes)

for i in range(2,len(primes)): #len(primes)=7(2,3,5,7,11,17,19)
    sum=0
    for j in primes:
        sum = sum+j
        if sum == primes[i]:
            count +=1
            break
print(count)