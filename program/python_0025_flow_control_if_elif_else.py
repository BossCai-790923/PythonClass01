# Requirement: base on user input age, tell the current user is a adult, a teenager, a kid or a baby.


age = int(input("How old are you? "))

# IMPORTANTCE !! ----------------------------------------
# if / elif / else gives you multiple choices.
# You can pick one path
# -------------------------------------------------------
if age >= 20:
    print("You are an adult now")
    print("You can start a software programmer career")
elif age >= 13:  # else if
    print("You are still a teenager")
    print("You should start taking some python lesson")
elif age > 3:
    print("You are still a kid")
    print("Play time at your age! Enjoy!")
else:
    print("You are still a baby")
    print("Eating, Drinking, Sleeping, Pooping, Crying ...")