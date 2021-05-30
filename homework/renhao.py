prime_numbers=[]
for number in range(2, 1001):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime_numbers.append(number)

print(prime_numbers)


for prime in prime_numbers:
    a = 2**(prime-1)
    for i in range(2, a):
        if a % i == 0:
            break
        if i == a-1 and a % a-1 != 0:
            print(a*((2**prime) - 1))
