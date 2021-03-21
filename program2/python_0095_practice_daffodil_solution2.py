'''
Logic:
1) 3 digits numbers range from 100 to 999, so I just need to loop in range(100,1000), check them 1 by 1
2) To convert to number to its unit / tens / hundreds digit, I can convert the number to str, then I use str index to calculat its value
'''

for i in range(100, 1000):

    i_str = str(i)

    '''
    i              is   int 123
    i_str          is   str '123'
    i_str[0]       is   str '1'      
    int(i_str[0])  is   int 1
    '''
    a = int(i_str[0])
    b = int(i_str[1])
    c = int(i_str[2])

    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)