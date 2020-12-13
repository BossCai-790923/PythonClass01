

a = 0
print('while loop starts:')

# IMPORTANT !!! -------------------------------------------
# break will terminate the current loop.
# break will make your loop stop immediately and move on to the next line of code
# ---------------------------------------------------------
while a < 5:
    a += 1
    if a == 3:
        break
    print(a)

print('While loop ends.')
