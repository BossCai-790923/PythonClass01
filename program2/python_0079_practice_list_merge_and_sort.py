'''
Requirement:
You have 2 SORTED lists, merge the 2 lists into 1 new list. And this new list is SORTED as well.

merge
list_a = [1,5,7,9,13,15,24,27,78,110,167]
list_b = [2,2,6,8,16,17,18,19,99]
to list_ab

merge
list_c = [1,5,7]
list_d = [2,2,6,8,16,17,18,19,99]
to list_cd

merge
list_e = []
list_f = [2,2,6,8,16,17,18,19,99]
to list_ef
'''


'''
Logic / Algorithm:
Step 1) I create 2 pointers index_a and index_b, they point to the 1st value of list_a and list_b
Step 2) I loop forever as I will break out of the loop myself
Stpe 3) In the loop body, there are 4 situations:

    Situation 1) list_a has reached the end, list_b has NOT reached the end.
    -> append the remaining values of list_b to new_list
       break the loop
    
    
    Situation 2) list_a has NOT reached the end, list_b has reached the end.
    -> append the remaining values of list_a to new_list
       break the loop
    
        
    Situation 3) list_a has reached the end, list_b has reached the end.
    -> break the loop
    
    
    Situation 4) list_a has NOT reached the end, list_b has NOT reached the end.
    -> I compare list_a[index_a] and list_b[index_b].
       I append the smaller value to my new list and move the index to the next
       
       
Question: How to tell whether list_a has reached the end?
Answer: if len(list_a) is 10, then list_a index value is 0 - 9.
        So when index_a == len(list_a), then index_a becomes invalid, then index_a is at the end of the list_a. 
'''


list_a = [1,5,7,9,13,15,24,27,78,110,167]
# list_a = [1,5,7]
# list_a = []
list_b = [2,2,6,8,16,17,18,19,99]


# Step 1) I define the 3 variables
new_list = []
index_a = 0
index_b = 0


while True:


    # Situation 1)
    if index_a == len(list_a) and index_b < len(list_b):
        new_list.extend(list_b[index_b:])
        break

    # Situation 2)
    if index_a < len(list_a) and index_b == len(list_b):
        new_list.extend(list_a[index_a:])
        break

    # Situation 3)
    if index_a == len(list_a) and index_b == len(list_b):
        break

    # Situation 4)
    if list_a[index_a] < list_b[index_b]:
        new_list.append(list_a[index_a])
        index_a += 1
    else:
        new_list.append((list_b[index_b]))
        index_b += 1

print(new_list)












