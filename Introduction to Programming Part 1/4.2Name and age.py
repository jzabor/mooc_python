'''
Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:

Sample output
What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
'''
fullname = input('What is your name? ')
yearofbirth = input('Which year were you born? ')
age2021 = 2021-int(yearofbirth)
print(f'Hi {fullname}, you will be {age2021} years old at the end of the year 2021')
