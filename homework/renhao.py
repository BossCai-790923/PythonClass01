primes = [2]
for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i-1:
            primes.append(i)
            break

number = int(input("type a number under 1000:"))
result = []
number_1 = number
while True:
    for prime in primes:
        if number_1 % prime == 0:
            result.append(prime)
            number_1 = number_1 / prime
            break
        else:
            continue
    if number_1 == 1:
        break

print(number, '=', end=' ')
for k in range(len(result)):
    if k == len(result) - 1:
        print(result[k])
    else:
        print(result[k], '*', end=' ')