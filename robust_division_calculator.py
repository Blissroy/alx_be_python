
python
def safe_divide(numerator, denominator):
    """
    Performs division of two numbers with proper error handling.
    
    Args:
        numerator: The numerator as a string (to be converted to float)
        denominator: The denominator as a string (to be converted to float)
        
    Returns:
        float: The result of division if successful
        str: Error message if division fails
    """
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
