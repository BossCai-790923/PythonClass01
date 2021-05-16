

buy_order = ('DBS', 100, 29.5, (2021, 5, 14, 10, 28, 7, 123))

# When unpacking, you may sometimes want to discard certain values.
# So you use underscore to represent, you don't need this value
_, shares, price, _ = buy_order

print(shares, price)


# another example
# In my loop body, I don't need this looping variable, so I can just use underscore to represent: I don't need it
for _ in range(10):
    print("Hello Python!")