vowels = list('aeiou')
word = input("Provide a word to search for vowels: ")

found = []

for letter in word:
    if letter in vowels:
        found.append(letter)
        letter_index = vowels.index(letter)
        vowels.pop(letter_index)

for vowel in found:
    print(vowel, end = ' ')