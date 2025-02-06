"""
hilly.py

Functions for converting within the Hilly (Pahadi) land measurement system
and between Hilly units and square meters.
"""

from .constants import HILLY_TO_SQ_M, HILLY_CONVERSION_FACTORS

def hilly_to_sq_meters(value: float, from_unit: str) -> float:
    """
    Convert a value from a Hilly land unit (ropani, aana, paisa, daam) to square meters.

    Args:
        value (float): The numeric amount to convert.
        from_unit (str): One of 'ropani', 'aana', 'paisa', 'daam'.

    Returns:
        float: The area in square meters.

    Raises:
        ValueError: If the from_unit is not recognized.

    Examples:
        Convert 2 ropanis to square meters:
        >>> hilly_to_sq_meters(2, 'ropani')
        1017.44

        Convert 10 aanas to square meters:
        >>> hilly_to_sq_meters(10, 'aana')
        317.9
    """
    unit_lower = from_unit.lower()
    if unit_lower not in HILLY_TO_SQ_M:
        raise ValueError(f"Unsupported Hilly unit: {from_unit}")
    return value * HILLY_TO_SQ_M[unit_lower]


def sq_meters_to_hilly(area_m2: float, to_unit: str) -> float:
    """
    Convert a value in square meters to a Hilly unit (ropani, aana, paisa, daam).

    Args:
        area_m2 (float): The area in square meters.
        to_unit (str): One of 'ropani', 'aana', 'paisa', 'daam'.

    Returns:
        float: The converted area in the requested Hilly unit.

    Raises:
        ValueError: If the to_unit is not recognized.

    Examples:
        Convert 508.72 square meters to ropanis:
        >>> sq_meters_to_hilly(508.72, 'ropani')
        1.0

        Convert 31.79 square meters to aanas:
        >>> sq_meters_to_hilly(31.79, 'aana')
        1.0
    """
    unit_lower = to_unit.lower()
    if unit_lower not in HILLY_TO_SQ_M:
        raise ValueError(f"Unsupported Hilly unit: {to_unit}")
    return area_m2 / HILLY_TO_SQ_M[unit_lower]


def hilly_to_hilly(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert directly between any two Hilly land units (ropani, aana, paisa, daam) using direct conversion factors.

    Args:
        value (float): The numeric amount in the from_unit.
        from_unit (str): The source Hilly land unit ('ropani', 'aana', 'paisa', 'daam').
        to_unit (str): The target Hilly land unit ('ropani', 'aana', 'paisa', 'daam').

    Returns:
        float: The converted value in the target Hilly unit.

    Raises:
        ValueError: If the from_unit or to_unit is not a recognized Hilly unit.
    """
    if from_unit not in HILLY_CONVERSION_FACTORS or to_unit not in HILLY_CONVERSION_FACTORS[from_unit]:
        raise ValueError("Invalid Hilly land unit provided.")
    
    return value * HILLY_CONVERSION_FACTORS[from_unit][to_unit]