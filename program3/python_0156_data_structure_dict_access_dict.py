car = {
    "brand": "BMW",
    "model": "X5",
    "year": 2021
}
print(car)

print("access the dictionary in 2 ways --------------------------")
car_model = car['model']
car_year = car['year']
print(car_model, car_year)

print(car.get('model'), car.get('year'))

print(car.get('price')) # None
print(car.get('price', 'key price does not exist')) # key price does not exist

# print(car['price']) # KeyError: 'price'


print('in - check if key exists in dict --------------------------')
if 'price' not in car:
    car['price'] = 2000000
print(f"car price is {car['price']}")


print("key 'year' already exists -> change value for key 'year'")
car['year'] = 2020
print(car)


print("key 'color' doesn't exist -> insert key / value pair into the dictionary")
car['color'] = 'red'
print(car)