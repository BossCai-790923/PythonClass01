# Requirement: I want to print a square with length = 5

# Example 1)
# Let's print a square with length = 2

# Shortcut key
# Duplicate current line: Ctrl+D
star_line = '*' * 2
print(star_line)
print(star_line)

separate_line = '-' * 50
print(separate_line)

star_line = '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)

# Shortcut key
# Move line Up or Down: Alt + Shift + Up /  Alt + Shift + Down
print(separate_line)

# I want the square do not close to the far left, I want it move to the middle. So,
# Step 1) 5 ' ' in the front
# Step 2) 5 '*' follows the 5 spaces


# Shortcut key:
# Copy - Ctrl + C
# Paste - Ctrl + V
star_line = ' ' * 5 + '*' * 5
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(star_line)
print(separate_line)

# I want to print a hollow square

# between the upper border and lower border, each line is
# 1) 5 ' ' in the left
# 2) 1 '*' (left border),  (5-2) spaces, and 1 '*' (right border)
left_star_right_star = ' ' * 5 + '*' + ' ' * 3 + '*'

print(star_line)
print(left_star_right_star)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)
print(separate_line)

# I want to print some letters
# I want to print PYTHON
# Each letter is in a rectangle 7 * 5

# Letter 'P'
# Total height: 7 lines

left_star = ' ' * 5 + '*' + ' ' * 4

#Shortcut key:
#Delete line: Ctrl + Y
print(star_line)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)
print(left_star)
print(left_star)
print(left_star)
print(separate_line)


# Letter 'Y'
# Total height: 7 lines

right_star = ' ' * 9 + '*'

print(left_star_right_star)
print(left_star_right_star)
print(left_star_right_star)
print(star_line)
print(right_star)
print(right_star)
print(star_line)
print(separate_line)



