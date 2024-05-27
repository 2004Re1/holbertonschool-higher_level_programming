def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.

    Examples:
    >>> add_integer(2, 3)
    5
    >>> add_integer(5.0, -2)
    3
    >>> add_integer(3.5, 2.5)
    6
    >>> add_integer(2.5, '3')
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer or b must be an integer
    """
    # Check if both a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b
