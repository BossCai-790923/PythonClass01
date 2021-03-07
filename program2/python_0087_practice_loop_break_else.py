'''
Requirement: find all prime numbers less than 100, using for loop - break - else
'''

# Step 1) I need to loop from 2 to 100, check all these numbers one by one.
for prime_candidate in range(2, 101):

    for potential_factor in range(2, prime_candidate):
        if(prime_candidate % potential_factor == 0):
            print(f"{prime_candidate} is not a prime number")
            break
    else:
        print(f"{prime_candidate} is a prime number")