"""
Generate docstrings for all the functions in this file.
"""
def add(a, b):
  """   Add two numbers and return the result.
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add.       
    Returns:
        int, float: The sum of the two numbers. 

  """      
    return a + b           
def multiply(a, b):
    """
    
    Multiply two numbers and return the result.
    Args:
        a (int, float): The first number to multiply.
        b (int, float): The second number to multiply.  

    Returns:
        int, float: The product of the two numbers.
    """
    return a * b
def divide(a, b):  
    """
    Divide one number by another and return the result.
    Args:
        a (int, float): The numerator.
        b (int, float): The denominator. Must not be zero.  
    Returns:
        float: The result of the division.  
    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Denominator must not be zero.")
    return a / b
def subtract(a, b):
    """ 
    Subtract one number from another and return the result.
    Args:
        a (int, float): The number to subtract from.
        b (int, float): The number to subtract.
    Returns:
        int, float: The result of the subtraction.
    """
    return a - b    
def power(base, exponent):
    """ 
    Raise a number to a power and return the result.
    Args:
        base (int, float): The base number.
        exponent (int, float): The exponent to raise the base to.
    Returns:
        int, float: The result of raising the base to the exponent.
    """
    return base ** exponent
def modulus(a, b):
    """ 
    Calculate the modulus of two numbers and return the result. 
    Args:
        a (int): The dividend.
        b (int): The divisor.   
    Returns:
        int: The remainder of the division of a by b.
    """
    return a % b
def square_root(x):
    """ 
    Calculate the square root of a number and return the result.
    Args:
        x (int, float): The number to calculate the square root of. Must be non-negative.         
    Returns:
        float: The square root of the number.   
    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return x ** 0.5