'''
https://baijiahao.baidu.com/s?id=1624782710246111037&wfr=spider&for=pc
'''

def find_primes(upper_bound):
    prime_number_list = []
    for prime_candidate in range(2, upper_bound):
        for potential_factor in range(2, prime_candidate):
            if prime_candidate % potential_factor == 0:
                break
        else:
            prime_number_list.append(prime_candidate)

    return prime_number_list


prime_list = find_primes(1000)
print(prime_list)

for prime in prime_list:
    number_1 = 2 ** prime - 1
    if number_1 > 1000:
        break
    if number_1 in prime_list:
        perfect_number = 2 ** (prime - 1) * number_1
        print(perfect_number)
