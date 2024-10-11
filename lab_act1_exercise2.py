# Exercise 2: Ohm’s Law Calculator
#Instructions:
#1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
#2.	Based on their choice, prompt the user to input the appropriate values.
#3.	Use Ohm's Law to calculate the missing variable and display the result.
#4.	Handle cases where division by zero might occur.

calWhat = str(input('What do you want to calculate; Voltage, Current or Resistance?'))

if calWhat == "Voltage":
    vCurrent = float(input('Enter the current:'))
    vResistance = float(input('Enter the resistance:'))
    calcVoltage = vCurrent * vResistance
    print('The voltage is ' + str(calcVoltage) + ' volts')

if calWhat == "Current":
    cVoltage = float(input('Enter the voltage:'))
    cResistance = float(input('Enter the resistance:'))
    calcCurrent = cVoltage / cResistance
    print('The current is ' + str(calcCurrent) + ' amperes')

if calWhat == "Resistance":
    rVoltage = float(input('Enter the voltage:'))
    rCurrent = float(input('Enter the current:'))
    calcResistance = rVoltage / rCurrent
    print('The resistance is ' + str(calcResistance) + ' ohms')  

else:
    print('Invalid input')
