a = 0
print("while loop starts:")

# IMPORTANT !!! ----------------------------------------
# continue will return to the beginning of the loop
# continue will ignore all remaining statements in the current iteration of the loop and move to the top of the loop
# ------------------------------------------------------
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)

print("while loop ends.")