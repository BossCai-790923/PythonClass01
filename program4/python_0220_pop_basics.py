'''
--------------------------------------------
Procedure Oriented Programming - POP
--------------------------------------------
All we learnt so far, they are all Procedure-Oriented Programming

What we did in our program?
Step 1) We define some variable (int / float / bool / list / set / tuple/ dict)
Step 2) We define some function (do_this() / do_that() / calculate_a_value(param) / populate_a_dict())
Step 3) Our main program begins (use variables & functions defined previously)
'''


# PREPARE DATA BEGIN -------------------------------
student_1 = {'name': 'Michael', 'score': 95}
student_2 = {'name': 'Bob', 'score': 81}

# FUNCTION DEFINITION BEGIN ------------------------
def say_score(student):
    print(f"Good morning Sir! My name: {student['name']}! my score is: {student['score']}")

# MAIN PROGRAM BEGIN -------------------------------
say_score(student_1)
say_score(student_2)