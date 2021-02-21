

scores = [85, 96, 77, 68]

#------------------------------
# Reverse a list
#------------------------------

# Solution 1: reverse()
scores.reverse()
print(scores) # [68, 77, 96, 85]

print("--------------------------------")

#------------------------------
# Sort a list
#------------------------------

# Solution 1: built-in function sorted()
sorted_scores = sorted(scores)
print(sorted_scores) # [68, 77, 85, 96]

# Shortcut key - Ctrl + Alt + V -> create variable
sorted_scores_reverse = sorted(scores, reverse=True)
print(sorted_scores_reverse) # [96, 85, 77, 68]

print(scores) # [68, 77, 96, 85]
# IMPORTANTCE !! ---------------------------------------------------------------------------------------------
# built-in function: sorted(my_list) will create a NEW list with my_list's sorted values.
# my_list is intact.
#-------------------------------------------------------------------------------------------------------------


# Solution 2: method sort()
scores.sort()
print(scores) # [68, 77, 85, 96]

scores.sort(reverse=True)
print(scores) # [96, 85, 77, 68]
# IMPORTANTCE !! ---------------------------------------------------------------------------------------------
# my_list.sort() will sort the values in my_list
# my_list is changed.
#-------------------------------------------------------------------------------------------------------------

