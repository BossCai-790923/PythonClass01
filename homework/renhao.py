list=[]
number = int(input())
list.append(number)
print(number)
number = int(input())
while True:
    if number != 'exit':
        for numbers in list:
            if number <= numbers:
                list.insert(list.index(numbers), number)
                print(list)
                break
            elif number > list[-1]:
                list.append(number)
                print(list)
                break
            else:
                continue
    number = int(input())