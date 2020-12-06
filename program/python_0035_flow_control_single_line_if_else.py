age = 15

if age < 18:
    kids_or_adult = 'kids'
else:
    kids_or_adult = 'adult'

# can be simplied into

kids_or_adult = 'kids'    if     age < 18     else       'adult'

# IMPORTANT !! ----------------------------------------------------------------------------------
# <value_when_true>    if     <boolean expression>      else       <value_when_false>
# -----------------------------------------------------------------------------------------------


# Example 2
fruit = 'apple'
isApple = True if fruit == 'apple' else False

# Example 3
x = 18
result = 'High' if x > 10 else 'Low'