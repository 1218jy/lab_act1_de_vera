# Exercise 1: Temperature Converter

#Create a program that converts temperatures between Celsius and Fahrenheit.
#Instructions:

#1.	Ask the user to input a temperature.
#2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
#3.	Perform the appropriate conversion and print the result.
temp = float(input('Enter a temperature to convert:'))

converType = input (str('Enter CF for Celsius to Fahrenheit and FC for Fahrenheit to Celsius:'))


ctof = ((temp*(5/9)+32))

ftoc = ((temp-32)*(5/9))

if converType == "CF":
    print('The converted temperature is:' + str(ctof) + 'F')
    
if converType == "FC":
    print(('The converted temperature is:' + str(ftoc) + ' C')) 

else:
    print('Invalid input')



