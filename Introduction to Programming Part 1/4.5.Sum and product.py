'''
Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

The program should function as follows:

Sample output
Number 1: 3
Number 2: 7
The sum of the numbers: 10
The product of the numbers: 21
'''

number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
numsum = number1 + number2
numprd = number1 * number2
print(f'The sum of the numbers: {numsum}\nThe product of the numbers: {numprd}')
