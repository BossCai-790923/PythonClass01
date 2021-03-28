# define a function
def describe_pet(animal_type, animal_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {animal_name}")


# call a function
describe_pet(animal_type='hamster', animal_name='harry')

# This is called keyword arguments
# You explicitly tell python, which argument is mapped to which parameter.

describe_pet(animal_name='billy', animal_type='dog')