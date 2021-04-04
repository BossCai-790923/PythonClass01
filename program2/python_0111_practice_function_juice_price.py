'''
Requirement:

A juice factory produces apple juice and orange juice in 2 containers - cube size and ball size
cube container has a edge length 10cm
ball container has a radius 6 cm

The factory use 2 materials - plastic / metal
So in total, the factory produces 8 kinds of beverage:
1) apple juice - cube container - plastic material
2) apple juice - cube container - metal material
3) apple juice - ball container - plastic material
4) apple juice - ball container - metal material
5) orange juice - cube container - plastic material
6) orange juice - cube container - metal material
7) orange juice - ball container - plastic material
8) orange juice - ball container - metal material

orange juice cost: 0.14 cent / cm^3
apple juice cost: 0.11 cent / cm^3
plastic material cost: 0.08 cent / cm^2
metal material cost: 0.18 cent / cm^2



These 8 kinds of juice are sold in NTUC supermarket and Cold Storage supermarket.
NTUC charges 10% of your juice price, meaning if your juice is sold at $2, you need to pay NTUC 20 cent.
Cold Storage changes 15% of your juice price, meaning if your juice is sold at $2, you need to pay Code Storage 30 cent.

There are in total 16 situations.

Remember: the factory also needs to make profit 30%

The factory manager asks you to help them to calculate the price for the above 16 situations, how much they should sell for each case.
'''

import math

'''
-------------------------------------
Step 1) Prepare all the data including
-------------------------------------

a) container
b) juice
c) material
d) supermarket

'''

container_1 = ['cube', 10]   # cube has a edge length 10 cm
container_2 = ['sphere', 6]  # sphere has a radius 6 cm
containers = [container_1, container_2]

juice_1 = ['orange', 0.14] # juice cost: 0.14 cent / cm^3
juice_2 = ['apple', 0.11] # juice cost: 0.11 cent / cm^3
juice = [juice_1, juice_2]

material_1 = ['plastic', 0.08] # container material cost: 0.08 cent / cm^2
material_2 = ['metal', 0.18] # container material cost: 0.18 cent / cm^2
material = [material_1, material_2]

ntuc = ['NTUC', 0.1] # NTUC charges 10% of your juice price
cold_storage = ['Cold Storage', 0.15] # Cold Storage charges 15% of your juice price
supermarkets = [ntuc, cold_storage]

# IMPORTANCE !!! --------------------------------------------------------
# List is good thing, it helps to group all related information together
# -----------------------------------------------------------------------

'''
-------------------------------------
Step 2) Core Logic:
-------------------------------------

Conclusion 1) 
Total situation = 2 juice * 2 container * material * 2 supermarket
                = 16 situations
                
I use nested loop to cover all 16 situations

for container in containers: 
    for current_juice in juice:
        for current_material in material:
            for supermarket in supermarkets:
                # here, we have 4 variables: container / current_juice / current_material / supermarket
                # my core logic is here
                
Conclusion 2)                                 
Inside the loop body, what shall we do? 
Step 1) Calculate the container's surface and volume.
        So we define a function:
        def surface_and_volume(container):
            pass

Step 2) Use container's surface and volume / juice / material to calculate the cost of the juice to the factory
       So we define a function:
       def calculate_cost(container_data, juice, material):
           pass            
           
Step 3) Because the factory needs to make 30% profit, so based on the cost to the factory, we can calculate the price so the supermarket.
      So we define a function:
      def sold_price_to_supermarket(cost):
         pass
         
Step 4) Because NTUC and Cold Storage need to make profit, so same import price from factory has a different selling price to customer。
     So we define a function:
     def sold_price_to_customer(cost, supermarket):
        pass                    
'''


def surface_and_volume(container):
    '''
    HOMEWORK

    :param container:
    :return:
    '''
    result = []

    if container[0] == 'cube':
        result.append(container[1] ** 2 * 6) # calculate surface area of cube
        result.append(container[1] ** 3)     # calculate volume of cube
    elif container[0] == 'sphere':
        result.append(4 * math.pi * container[1] ** 2)   # calculate surface area of sphere
        result.append(4/3 * math.pi * container[1] ** 3) # calculate volume of sphere
    else:
        print(f"Unknown object type: {container[0]}")

    return result



def calculate_cost(container_data, juice, material):
    '''
    calculate the cost for the juice

    :param container_data: is a list <br>
           container_data[0] is the surface area of the container <br>
           container_data[1] is the volume of the container. <br>

    :param juice: is a list <br>
           juice[0] is the juice type, it can be either 'apple' or 'orange'
           juice[1] is the juice price, how much does it cost per cm^3

    :param material: is a list <br>
           material[0] is the material type, it can be either 'plastic' or 'metal'
           material[1] is the material price, how much does it cost per cm^2

    :return:  the total cost of the juice. Including juice cost + container cost
    '''
    container_cost = container_data[0] * material[1]
    juice_cost = container_data[1] * juice[1]
    total_cost = container_cost + juice_cost
    return total_cost


def sold_price_to_supermarket(cost):
    '''
    HOMEWORK

    :param cost:
    :return:
    '''
    return cost * 1.3


def sold_price_to_customer(cost, supermarket):
    '''
    HOMEWORK

    :param cost:
    :param supermarket:
    :return:
    '''
    return cost * (1 + supermarket[1])



for container in containers:
    for current_juice in juice:
        for current_material in material:
            for supermarket in supermarkets:
                print(f"For juice type: container: {container}, juice: {current_juice}, material: {current_material}, supermarket: {supermarket}")
                container_info = surface_and_volume(container)
                print(f"Surface area: {container_info[0]:.2f} cm^2")
                print(f"Volume: {container_info[1]:.2f} cm^3")
                original_cost = calculate_cost(container_info, current_juice,current_material)
                print(f"Cost for the factory to produce the juice: ${original_cost/100:.2f}")
                selling_price_to_supermarket = sold_price_to_supermarket(original_cost)
                print(f"Selling price to the supermarket: ${selling_price_to_supermarket/100:.2f}")
                selling_price_to_customer = sold_price_to_customer(selling_price_to_supermarket, supermarket)
                print(f"Selling price to the cusomter: ${selling_price_to_customer/100:.2f}")
                print('-' * 100)
