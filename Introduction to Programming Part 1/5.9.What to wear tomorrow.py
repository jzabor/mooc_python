'''
Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

Some examples of expected behaviour:

Sample output
What is the weather forecast for tomorrow?
Temperature: 21
Will it rain (yes/no): no
Wear jeans and a T-shirt

Sample output
What is the weather forecast for tomorrow?
Temperature: 11
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well

Sample output
What is the weather forecast for tomorrow?
Temperature: 7
Will it rain (yes/no): no
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you

Sample output
What is the weather forecast for tomorrow?
Temperature: 3
Will it rain (yes/no): yes
Wear jeans and a T-shirt
I recommend a jumper as well
Take a jacket with you
Make it a warm coat, actually
I think gloves are in order
Don't forget your umbrella!
'''

print('What is the weather forecast for tomororow?')
temp = int(input('Temperature: '))
weather = input('Will it rain (yes/no): ')

if temp > 20:
    print('Wear jeans and a T-shirt')
elif temp > 10:
    print('Wear jeans and a T-shirt')
    print('I recommend a jumper as well')
elif temp > 5:
    print('Wear jeans and a T-shirt')
    print('I recommend a jumper as well')
    print('Take a jacket with you')
elif temp <= 5:
    print('Wear jeans and a T-shirt')
    print('I recommend a jumper as well')
    print('Take a jacket with you')
    print('Make it a warm coat, actually')
    print('I think gloves are in order')
if weather == 'yes':
    print("Don't forget your umbrella!")
