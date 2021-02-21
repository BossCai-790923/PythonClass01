



# But, Wenxi's requirement is '可以把 all of pi 的 numbers 写出来吗？'
# It seems like, Wenxi is asking a lot of numbers after decimal point.
# The above one can only print 15 digits.


# Luckily, we have learnt Python f string, so we can try print 100 digits after decimal point.
print(f'{math.pi:.100f}') # 3.1415926535897931159979634685441851615905761718750000000000000000000000000000000000000000000000000000

# Now it better, we can see 49 digits after decimal point. Then a lot of zero after that.
# Conclusion: Python only keeps 49 digits after decimal point for pi in python math module


# Then I find this:
# https://www.mathscareers.org.uk/calculating-pi/
# This is a really fun article!
# Especially I read this: In fact if you search long enough within the digits of Pi (π) you can find any number, including your birthday.

# the article introduces 3 ways to teach you how to calculate pi. The most useful for us is the 3rd way:
# pi / 4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ...
# Let's try this:


# Step 1) I define a variable quarter_of_pi
quarter_of_pi = 0

# Step 2) Then I loop and calculate quarter_of_pi, let's calculate 100,000 entries first.

# Let's summarize the relationship between my looping variable index and entry
# index = 0  -> entry = 1    ->  1 / (2 * index + 1)
# index = 1  -> entry = 1/3  ->  1 / (2 * index + 1)
# index = 2  -> entry = 1/5  ->  1 / (2 * index + 1)
# index = 3  -> entry = 1/7  ->  1 / (2 * index + 1)
# ... ...

# We also need a value to control +/-
positive = 1

for index in range(100):
    entry = 1 / (2 * index + 1)
    quarter_of_pi += entry * positive
    positive *= -1 # switch positive to -1, so that next entry becomes minus

value_of_pi = quarter_of_pi * 4
print(f"{value_of_pi:.100f}")

# There is 1 problem with this algorithm:





