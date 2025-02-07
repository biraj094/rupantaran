"""
cross_system.py

Functions for converting between Terai land units and Hilly land units
by leveraging square meters as the common intermediary.
"""

from .terai import terai_to_sq_meters, sq_meters_to_terai
from .hilly import hilly_to_sq_meters, sq_meters_to_hilly


def terai_to_hilly(
    value: float, from_unit: str, to_unit: str, precision: int = 4
) -> float:
    """
    Convert from a Terai unit (bigha, kattha, dhur) to a Hilly unit
    (ropani, aana, paisa, daam).

    Args:
        value (float): Amount in the Terai unit.
        from_unit (str): One of 'bigha', 'kattha', 'dhur'.
        to_unit (str): One of 'ropani', 'aana', 'paisa', 'daam'.
        precision (int, optional): The number of decimal places for output (default is 4).

    Returns:
        float: Converted value in the Hilly unit rounded to the specified precision.

    Raises:
        ValueError: If either from_unit or to_unit is not recognized or value is not numeric.

    Examples:
        Convert 1 bigha to ropanis:
        >>> terai_to_hilly(1, 'bigha', 'ropani')
        13.3100

        Convert 10 katthas to aanas:
        >>> terai_to_hilly(10, 'kattha', 'aana', precision=2)
        6.23
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")

    # Convert to square meters first
    area_m2 = terai_to_sq_meters(value, from_unit)
    # Convert square meters to the Hilly unit
    return round(sq_meters_to_hilly(area_m2, to_unit), precision)


def hilly_to_terai(
    value: float, from_unit: str, to_unit: str, precision: int = 4
) -> float:
    """
    Convert from a Hilly unit (ropani, aana, paisa, daam) to a Terai unit
    (bigha, kattha, dhur).

    Args:
        value (float): Amount in the Hilly unit.
        from_unit (str): One of 'ropani', 'aana', 'paisa', 'daam'.
        to_unit (str): One of 'bigha', 'kattha', 'dhur'.
        precision (int, optional): The number of decimal places for output (default is 4).

    Returns:
        float: Converted value in the Terai unit rounded to the specified precision.

    Raises:
        ValueError: If either from_unit or to_unit is not recognized or value is not numeric.

    Examples:
        Convert 1 ropani to bighas:
        >>> hilly_to_terai(1, 'ropani', 'bigha')
        0.0750

        Convert 16 daams to dhurs:
        >>> hilly_to_terai(16, 'daam', 'dhur', precision=2)
        0.94
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")

    # Convert to square meters first
    area_m2 = hilly_to_sq_meters(value, from_unit)
    # Convert square meters to the Terai unit
    return round(sq_meters_to_terai(area_m2, to_unit), precision)
