'''
Print all 3 digits 'daffodil numbers'.
A 'daffodil number' means
the cube of the number's unit digit +
the cube of the number's tens digit +
the cube of the number's hundreds digit = the number itself

For example:
153 = 1 ** 3 + 5 ** 3 + 3 ** 3
'''

'''
Logic:
1) 3 digits numbers range from 100 to 999, so I just need to loop in range(100,1000), check them 1 by 1
2) To convert to number to its unit / tens / hundreds digit, I can use modulus and floor division
'''

for i in range(100, 1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10

    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)