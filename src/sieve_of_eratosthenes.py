limit_number = int(input(
    "Type in any number to find all prime numbers within it's range : "))

if limit_number <= 1:
    print (f'{limit_number} is not a primary number')
    exit()
    
prime = [n for n in range(2, limit_number+1)]
p = 2

while (p * p <= limit_number):

    for i in range(p * 2, limit_number + 1, p):
        if i in prime:
            prime.remove(i)
    p += 1

print(prime)

