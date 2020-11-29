float_a = float(input("Number a: "))
float_b = float(input("Number b: "))
operator = input("Operator: ")


# IMPORTANT !!! -------------------------------------------
# if / elif / else Review:
# 1) There is NOTHING after colon(:)
#    AFter you type colon(:), press 'ENTER' key immediately
#    PyCharm will help you indent 4 spaces automatically
# 2) 'elif' means 'else if'. Python makes it short, just use 'elif'.
# ---------------------------------------------------------
if operator == '+':
    result = float_a + float_b
elif operator == '-':
    result = float_a - float_b
elif operator == '*':
    result = float_a * float_b
elif operator == '/':
    if float_b == 0:
        print("Wrong input, please try again.")
    else:
        result = float_a / float_b
elif operator == '**':
    result = float_a ** float_b
else:
    print(f"Unrecognized operator {operator}")
    result = 0

print(f"{float_a} {operator} {float_b} = {result:.2f}")
