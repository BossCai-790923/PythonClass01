'''
Requirement:
you have a long, sorted tuple, which contains the scores of the whole class.
You need to remove the lowest and the highest scores, and get an average score of the whole class.
'''

grades = (55, 57, 60, 67, 77, 78, 79, 83, 85, 99, 100)

# Solution 1) slice
middle_score = grades[1:-1]
print(type(middle_score))
print(sum(middle_score) / len(middle_score))

# Solution 2) unpacking - star variable in the middle
lowest, *middle_score, highest = grades
print(type(middle_score))
print(sum(middle_score) / len(middle_score))


# EXAMPLE 2: unpacking a list -------------------------------------

# start variable in the last
record1 = ['Dave', 'dave@hotmail.com', '91234567', '61234567', '81234567']
name, email, *phone_numbers = record1
print(phone_numbers)

record2 = ['Billy', 'billy@hotmail.com']
name, email, *phone_numbers = record2 # unpacking here generates an empty list
print(phone_numbers)

record3 = ['Dave', 'dave@hotmail.com', '91234567']
name, email, *phone_numbers = record3 # unpacking here generates a list which contains 1 value only
print(phone_numbers)



# EXAMPLE 3: use together with throwaway variable -----------------------

tuple_numbers = 1,2,3,4,5,6,7,8,10,100

lowest, *_, highest = tuple_numbers
print(lowest, highest)

*_, second_high, first_high = tuple_numbers
print(second_high, first_high)


'''
-------------------
Summary
-------------------
1) unpacking can be applied to either a tuple or a list
2) unpacking is very useful when you to try to group a part of a list / a tuple, into a new list
'''

