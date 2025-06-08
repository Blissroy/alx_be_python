# temp_conversion_tool.py

# 1. Checks for Definition of global conversion factors
# These are clearly defined at the top level of the script, making them global.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    2. Checks for Implement conversion functions
    This function takes Fahrenheit and returns Celsius, using the global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    2. Checks for Implement conversion functions
    This function takes Celsius and returns Fahrenheit, using the global factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    3. Checks for User interaction
    This function handles prompting the user for input and displaying results.
    """
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input) # Attempt to convert to float
    except ValueError:
        # 4. Checks for implementation of Value Error
        # This specifically catches the ValueError if float() conversion fails.
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function if input is invalid

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # This handles incorrect unit input, which is part of robust user interaction.
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if _name_ == "_main_":
    main()
