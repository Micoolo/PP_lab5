"""Binary converter utility functions."""


def to_binary(number: int) -> str:
    """Convert an integer in range <0, 100> to its binary representation as a string."""
    if not isinstance(number, int):
        raise TypeError("number is not integer")
    if number < 0 or number > 100:
        raise ValueError("number must be in <0, 100> range")
    return bin(number)[2:]
