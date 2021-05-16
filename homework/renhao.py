base = int(input('input base number:'))
count = int(input('input entry count:'))
result = base
for i in range(count - 1):
    result = result + (result * 10)

print(result)