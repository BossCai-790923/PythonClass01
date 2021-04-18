input_num = int(input("Please input a number to be factorised: "))
factor = 2
myList = []

while input_num != 1:
    if (input_num % factor) == 0:
        input_num = input_num / factor
        myList.append(factor)
    else:
        factor += 1

for i in range(len(myList)-1):
    print(f"{myList[i]} * ", end='')
print(myList[-1])

'''
范老师点评：
1. 家锐的代码值得大家一读。
2. 优点在于，代码写得非常整洁，简练，容易理解。 只需要短短14行。而范老师的代码需要40-50行（不包括comments)。
3. 缺点在于，a) worst case, 他的代码需要尝试从2到input_num 这么多次。性能不好。
           b) 如果input_num is prime number, 那么输出的时候,忽略了 1 * 的部分。

4. 范老师的代码和家锐同学的代码各有优缺点。
   目前我们Python学习的重点是: 
   '学习使用function,来把一个大的问题，切割成小的问题，采用divide-and-conquer策略'.
   所以仍旧要follow 范老师的代码。 
'''