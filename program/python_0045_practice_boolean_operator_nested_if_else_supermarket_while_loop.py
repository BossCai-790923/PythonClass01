welcome_msg = '''
*************************************
    Welcome to NTUC Supermarket
*************************************
'''

print(welcome_msg)

product_prices = '''
----------------------
beef - $20 / kg
pork - $16 / kg
tomato - $5 / kg
apple - $5 for 5 apples; $1.6 each   
orange - $5 for 3 oranges; $2 each   
----------------------
'''

print(product_prices)


'''
What I need you to do: use while loop, so that customer can buy multiple products
HINT:
 1) An extra option 'EXIT' is required to let customer to exit the 'buy product' while loop
    The program is composed of
    a) welcome customer
    b) buy product
    c) check member
    d) payment

    the loop should happen only at b)

'''


# put init value so that the code logic is complete
product_name = ''
total_price_for_all_products = 0

# IMPORTANT!!! --------------------------------------------------------------------------------------
# You need to indent the whole section 4 spaces to the right! So that it goes under the while loop!
# You need to indent the whole section 4 spaces to the right! So that it goes under the while loop!
# You need to indent the whole section 4 spaces to the right! So that it goes under the while loop!
# ---------------------------------------------------------------------------------------------------
while product_name != 'exit':

    product_name = input("What product do you want to buy (beef / pork / tomato / apple / orange / exit): ")

    total_price = 0

    if product_name == 'beef' or product_name == 'pork' or product_name == 'tomato':

        total_weight = float(input("Total weight(kg): "))

        if product_name == 'beef':
            unit_price = 20 # $20 / kg
        elif product_name == 'pork':
            unit_price = 16 # $16 / kg
        else:
            unit_price = 5 # $5 / kg

        total_price = unit_price * total_weight
        print(f'{product_name} : ${unit_price} * {total_weight} = ${total_price}')

    elif product_name == 'apple' or product_name == 'orange':

        # 1st step
        # ask the customer, how many you buy
        total_count = int(input("Total quantity: "))

        if product_name == 'apple':

            # 2nd step
            # calculate price
            # the key here is to group apples into 5, see how many groups it has, how many are left
            group_count = total_count // 5
            single_count = total_count % 5

            group_price = 5
            single_price = 1.6

        else:

            # 2nd step
            # calculate price
            # the key here is to group apples into 5, see how many groups it has, how many are left
            group_count = total_count // 3
            single_count = total_count % 3

            group_price = 5
            single_price = 2

        group_price_total = group_price * group_count
        single_price_total = single_price * single_count
        total_price = group_price_total + single_price_total

        # 3rd step
        # Tell customer
        print(f'{product_name} : ${total_price}')


    elif product_name == 'exit':
        break

    else:
        print(f'Unrecognized product : {product_name}')

    total_price_for_all_products += total_price


















# membership -------------------------------------------------------------------------------
member_str = input("Are you a member? ")

if member_str == 'Y' or member_str == 'y' or member_str == 'Yes' or member_str == 'yes':
    total_price_for_all_products *= 0.9 # equals to total_price = total_price * 0.9
    print(f'After discount, total price: ${total_price_for_all_products}')

# payment ----------------------------------------------------------------------------------
payment = input("Will you pay using Visa / Mastercard / NETS / Cash? ")
if payment == 'Visa' or payment == 'Mastercard':
    signature = input("Please sign your name: ")
    print(f'Signature {signature} is well received.')
    print(f'${total_price_for_all_products} has been charged to your {payment} card')
elif payment == 'NETS':
    password = input("Please input your NETS card password:")
    print(f'${total_price_for_all_products} has been charged to your NETS card')
else:
    total_paid = float(input("How much will you pay? : "))
    if total_paid > total_price_for_all_products:
        print(f'Here comes your change: ${total_paid - total_price_for_all_products}')
    elif total_paid < total_price_for_all_products:
        print(f'You are still short of ${total_price_for_all_products - total_paid}. I am sorry, I cannot give your {product_name}')
    else:
        print(f"You've paid the exact amount.")



bye_msg = '''
**********************
    See you again!
**********************
'''

print(bye_msg)
