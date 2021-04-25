text1 = 'welcome to the jungle'
word_list1 = text1.split()  # ['welcome', 'to', 'the', 'jungle']
print(word_list1)

text2 = "Hello, my name is Peter, I am 26 years old"
word_list2 = text2.split(", ") # ['Hello', 'my name is Peter', 'I am 26 years old']
print(word_list2)
word_list2 = text2.split(",") # ['Hello', ' my name is Peter', ' I am 26 years old']
print(word_list2)

text3 = "apple#banana#cherry#orange"
word_list3 = text3.split("#") # ['apple', 'banana', 'cherry', 'orange']
print(word_list3)