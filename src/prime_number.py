n = int(input("Enter a number: "))

if (n <= 1):
    print(f'{n} is not a prime number')
    
if (n == 2):
    print(f'{n} is a prime number')

if (n > 2):
    for i in range(2, n):
        if n%i == 0:
            print(f'{n} in not a prime number')
            exit()
    print(f'{n} is a prime number')



        
        
        

