'''
Requirement:
User will supply a word from console.
Requirement 1) You need to find all the vowels(a/e/i/o/u) in the word.
Requirement 2) Further enhance your code, only collect vowels once (we don't want duplicate vowels)
'''

# Step 0) preparation work
vowels = list('aeiou')
word = input("Provide a word to search for vowels: ")


# Step 1) Because I need to find all vowels in the word, so I need to create a new empty list to hold all vowels found in the word
found = []

# Step 2) I loop all the characters in the word to check whether it is a vowel.
# ATTENTION: loop a str value
for letter in word:

    # Step 2.1) if the letter is a member of vowels list, then I append it to the list variable - found
    if letter in vowels:
        if letter not in found:
            found.append(letter)


# Step 3) I print the list - found
# ATTENTION: loop a list value
for vowel in found:
    print(vowel, end = ' ')