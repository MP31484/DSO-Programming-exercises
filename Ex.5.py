'''
Exercise 5
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''


string= input('Is it a palindrome? ')
reversed=(string [::-1])
if string == reversed:
    print('Your word is a palindrome!')
else:
    print('It is not :( ')