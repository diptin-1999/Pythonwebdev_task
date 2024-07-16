#conversion between 
#F=int(input("Enter the temperature in fahrenheit:"))
#if C=(F-32)*5/9
#print("Temperature in celcius",C)#

unit = int(input("is this a temperature in celsius or fahrenhit(C/F):"))
temp = float(input("Enter the temperature:"))

if unit == "C":
    ntemp = 9 / 5 * temp + 32
    print("Temperature in celsius:",ntemp)
elif unit == "F":
      ntemp = 5 / 9 * (temp-32)
      print("Temperature in Fahrenheit:",ntemp)
else:
    print("invalid unit", unit)
         
         