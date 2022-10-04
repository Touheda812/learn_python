'''
Strings are immutable
backslash(\) used to escape quotes
raw strings\
span string multiple lines
print multiple times using *
concatenate using +
string indexing and slicing
string methods: capitalize(), casefold(), center(width[,fillchar])
'''
# print('doesn't') SyntaxError: unterminated string literal
print('doesn\'t')
print("doesn't")
print('"Yes,"they said.')  # sigle quote
print("\"Yes,\" they said.")
s = 'First line.\nSecond line.'
print(s)

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by
# adding an r before the first quote
# Raw strings
print('C:\house is\nice')
print(r'C:\house is\nice')

# span strings: multiple lines
print("""
Hello Maria,
    How r you 
Hope you r fine""")

# print multiple times
print(3 * 'Touheda' + 'Khanom')
print(3 * ('Touheda' + 'Khanom'))

# Put several strings within parentheses to have them joined together.
text = ("This is the most "
        "important thing.")
print(text)

# Concatenate variables and literal using +
txt = 'py'
print(txt + 'thon')

# indexing
print('----------String Indexing-----------')
word = 'Touheda'
print(word[0])  # first character
print(word[5])
print(word[-1])  # last character
print(word[-6])
print('Length of the word is:', len(word))

print('-----String Slicing------')
print(word[0:2])
print(word[2:7])

print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end

print(word[:2] + word[2:])

# create new string
print('J' + word[1:])

# String Methods
# capitalize
string = 'mother'
print('capitalize string:', string.capitalize())

# lower case
string_1 = 'Father'
print('lowercase string:', string_1.casefold())

# center
string_2 = 'This is the book'
print(string_2.center(50))

# Title()
print('hello world'.title())
print("they're bill's friends from the UK".title())

# split()
print('1,2,3'.split())
print('1<>2<>3'.split('<>'))

print(string_2.swapcase())
# output("tHIS IS THE BOOK")
