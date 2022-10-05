'''
Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

num = int(input('Pick a number: '))
num2 = int(input('Pick another number: '))

#if num % 4 == 0:
 #   print('Your number is divisible by 4.')
#elif num % 2 == 0:
 #   print('Your number is an even number.')
#else:
 #   print('Your number is an odd number.')

if num % num2 == 0:
    print('Your numbers are divisible by each other')
else:
    print('The numbers you have chosen are not divisible by each other')



