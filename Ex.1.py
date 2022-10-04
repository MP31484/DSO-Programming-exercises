'''
Exercise 1
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

name = input('What is your name? ')
age = int(input('What year were you born in? '))
num = int(input('How many times would you like the message to be repeated? '))

year_100 = age+100


print(('Hello, ' + name + ' you will turn 100 years of age in '+ str(year_100)+'\n')*num)



