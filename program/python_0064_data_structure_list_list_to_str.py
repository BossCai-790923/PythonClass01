animals = ['tiger', 'elephant', 'snake', 'shark']


# ------------------------------------
# Convert list to str using join() method
# ------------------------------------
animals_str_1 = ''.join(animals)
print(animals_str_1) # tigerelephantsnakeshark
animals_str_2 = ','.join(animals)
print(animals_str_2) # tiger,elephant,snake,shark
animals_str_3 = '|'.join(animals)
print(animals_str_3) # tiger|elephant|snake|shark