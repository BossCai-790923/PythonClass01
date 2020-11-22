# We have some students, base on their math / science / english score, we will assign them to the following classes
# Elite Class - all 3 subjects should have score higher than 85
# Math Elite Class - Math score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
# Science Elite Class - Science score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
# English Elite Class - English score higher than 85 and 3 subjects average higher than 75 and no subject lower than 70
# Express Class - average score higher than 75 and no subject lower than 65
# Normal Class - other students

# Step 0) Get score from console -----------------------
math_score = float(input("Math score: "))
science_score = float(input("Science score: "))
english_score = float(input("English score: "))

# Step 1) Calculate average score ----------------------
average_score = (math_score + science_score + english_score) / 3
print(f'Your average score is {average_score:.2f}')


# Step 2) Check eligibility for Elite Class
if math_score > 85 and science_score > 85 and english_score > 85:
    class_name = 'Elite Class'

# IMPORTANTCE !!! ---------------------------------------------------------------------------------
# Nested if / elif / else - you can put if/elif/else under if clause or elif clause or else clause
# -------------------------------------------------------------------------------------------------
# Step 3) Check eligibility for Math Elite / Science Elite / English Elite Class
elif (math_score > 85 or science_score > 85 or english_score > 85) and average_score > 75 and math_score >= 70 and science_score >= 70 and english_score >=70:
    if math_score > 85:
        class_name = 'Math Elite Class'
    elif science_score > 85:
        class_name = 'Science Elite Class'
    else: # english_score > 85
        class_name = 'English Elite Class'

# Step 4) Check eligibility for express class
elif average_score > 75 and math_score >=65 and english_score >= 65 and science_score >= 65:
    class_name = 'Express Class'

# Step 5) assigned to normal class
else:
    class_name = 'Normal Class'

print(f"You are assigned to {class_name}")