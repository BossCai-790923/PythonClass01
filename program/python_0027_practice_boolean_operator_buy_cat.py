# Requirement: A customer walks into a Pet's store, he said, 'I want a
# male cat, white or yellow
# Or a female cat, not white
# Or just a black cat
# You need to get input from console about cat gender and cat color
# Your program needs to tell whether the customer wants it or not

gender = input("Is the cat male or female? ")
color = input("What's the color of the cat? ")


# 1) gender == 'male' and (color == 'white' or color == 'yellow')
# or
# 2) gender == 'female' and not color == 'white'
#                 you can also code in this way: gender == 'female' and color != 'white'
# or
# 3) color == 'black'

if gender == 'male' and (color == 'white' or color == 'yellow') or gender == 'female' and not color == 'white' or color == 'black':
    print("I will take it")
else:
    print("I don't want it")