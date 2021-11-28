import math

print('Convert degree to radians ---------------------------------')
print(f"radians(360) equals {math.radians(360):.2f}, which is same as {2 * math.pi:.2f}")
print(f"radians(180) equals {math.radians(180):.2f}, which is same as {1 * math.pi:.2f}")
print(f"radians(90)  equals {math.radians(90):.2f}, which is same as {1/2 * math.pi:.2f}")
print(f"radians(45)  equals {math.radians(45):.2f}, which is same as {1/4 * math.pi:.2f}")
print(f"radians(30)  equals {math.radians(30):.2f}, which is same as {1/6 * math.pi:.2f}")
print(f"radians(-90) equals {math.radians(-90):.2f}, which is same as {-1/2 * math.pi:.2f}")

print('sin -------------------------------------------------------')
print(f"sin(360) equals {math.sin(math.radians(360)):.2f}")
print(f"sin(180) equals {math.sin(math.radians(180)):.2f}")
print(f"sin(90)  equals {math.sin(math.radians(90)):.2f}")
print(f"sin(45)  equals {math.sin(math.radians(45)):.2f}")
print(f"sin(30)  equals {math.sin(math.radians(30)):.2f}")
print(f"sin(-90) equals {math.sin(math.radians(-90)):.2f}")

print('cos -------------------------------------------------------')
print(f"cos(360) equals {math.cos(math.radians(360)):.2f}")
print(f"cos(180) equals {math.cos(math.radians(180)):.2f}")
print(f"cos(90)  equals {math.cos(math.radians(90)):.2f}")
print(f"cos(45)  equals {math.cos(math.radians(45)):.2f}")
print(f"cos(30)  equals {math.cos(math.radians(30)):.2f}")
print(f"cos(-90) equals {math.cos(math.radians(-90)):.2f}")
