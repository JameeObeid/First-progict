#------4---------

Str = input("Enter the file name with extension: ")
Fullstop = Str.find('.')

print("The file extension is:", Str[Fullstop + 1:])

#------1---------

Str = input("Enter a sentence: ")
letter = Str.lower().find("e")
print("The character 'e' is at position", letter, "in the sentence")
while True:
    letter = Str.lower().find("e", letter + 1)
    if letter == -1:
        break


    print("The character 'e' is at position", letter, "in the sentence")

#------3---------

Str = input("Enter a sentence: ")
letter = Str.lower()
vowels_a = letter.count('a')
vowels_o = letter.count('o')
vowels_e = letter.count('e')
vowels_i = letter.count('i')
vowels_u = letter.count('u')
vowels_y = letter.count('y')


print("The numbers of vowels in the string: ", vowels_o + vowels_i + vowels_u + vowels_y + vowels_e + vowels_a)

#------2---------

Str = input("Enter a word:")
def place (letter):
    letter_x1 = letter[0]
    letter_x2 = letter[-1]
    Finsh_word = letter_x2 + letter[1:-1] + letter_x1


    print(Finsh_word)


place (Str)

#------5---------

Str = input("Enter any word: ")
def place (x):
    letter_x1 = x[-1:0]
    letter_x2 = x[-1:0]
    Finsh_word = letter_x2 + x[::-1] + letter_x1

    print(Finsh_word)


place(Str)

