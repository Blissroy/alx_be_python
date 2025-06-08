# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius
    using the global conversion factor
    """
    return (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit
    using the global conversion factor
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_OFFSET

def main():
    print("Temperature Conversion Tool")
    
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input and validate
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        while unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' or 'F'.")
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Perform conversion
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        else:
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
            
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

if _name_ == "_main_":
    main()
