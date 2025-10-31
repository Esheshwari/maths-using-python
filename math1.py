# Write a Python program to form all 2-letter "words" using
# the alphabets A, B, and C, allowing repetition.

#list of alphabets
alphabets = ['A', 'B', 'C']

print("All possible 2-letter words (with repetition):")
#outer loop selects the first letter
for first_letter in alphabets:
#inner loop selects the second letter
    for second_letter in alphabets:
        print(first_letter + second_letter)
