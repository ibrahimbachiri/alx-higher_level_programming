def print_square(size):
    """
    Print a square with the character '#' of the given size.

    Args:
        size (int): The size (side length) of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float and less than 0.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        if isinstance(size, float):
            if size < 0:
                raise TypeError("size must be an integer")
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

# Test cases
if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
