
def ArctanDenom(d, ndigits):
    term = (10 ** ndigits) // d
    total = term

    n = 0
    while term != 0:
        n += 1
        term //= (-d * d)
        total += (term // (2 * n + 1))

    return total


ndigits = 100000

# https://en.wikipedia.org/wiki/John_Machin
# Use John Machin's Formula to calculate pi.
pi = 4 * (4 * ArctanDenom(5, ndigits) - ArctanDenom(239, ndigits))

print(pi)

print(str(pi).find('19800203'))