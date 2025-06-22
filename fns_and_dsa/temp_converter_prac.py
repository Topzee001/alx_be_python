# fahrenheit = cel * (9/5) + 32
# celsius = (fah - 32) * 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    # print(f"{fahrenheit}˚F conversion to celsius is: {celsius}˚C")
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    # print(f"{celsius}˚C conversion to fahrenheit is: {fahrenheit}˚F")
    return fahrenheit


try:

    temp = float(input("Enter the temperature to convert: "))
    c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if c_or_f == "F":     
        result = convert_to_celsius(temp)
        print(f"{temp}˚F is {result}˚C")
    elif c_or_f == "C":       
        result = convert_to_fahrenheit(temp)
        print(f"{temp}˚C is {result}˚F")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

except ValueError as e:
    print("Error", e)

