# Requirement: calculate the sum from 1 to 100

# Solution 1 - use simple for range loop
sum_value_for_solution1 = 0

for i in range(1, 101):
    sum_value_for_solution1 += i

print(f"Sum from 1 to 100 is {sum_value_for_solution1}")

# Solution 2 - use built-in function sum
sum_value_for_solution2 = sum(range(1,101))
print(f"Sum from 1 to 100 is {sum_value_for_solution2}")
