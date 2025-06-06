'''
Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B
'''

a = input("Enter the first letter: ")
b = input("Enter the second letter: ")
c = input("Enter the third letter: ")


if a > b:
    if a < c:
        middle = a
    elif b > c:
        middle = b
    else:
        middle = c
else:
    if a > c:
        middle = a
    elif b < c:
        middle = b
    else:
        middle = c

print("The letter in the middle is", middle)
