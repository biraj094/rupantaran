"""
cross_system.py

Functions for converting between Terai land units and Hilly land units
by leveraging square meters as the common intermediary.
"""

from .terai import terai_to_sq_meters, sq_meters_to_terai
from .hilly import hilly_to_sq_meters, sq_meters_to_hilly

def terai_to_hilly(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert from a Terai unit (bigha, kattha, dhur) to a Hilly unit
    (ropani, aana, paisa, daam).

    Args:
        value (float): Amount in the Terai unit.
        from_unit (str): One of 'bigha', 'kattha', 'dhur'.
        to_unit (str): One of 'ropani', 'aana', 'paisa', 'daam'.

    Returns:
        float: Converted value in the Hilly unit.

    Raises:
        ValueError: If either from_unit or to_unit is not recognized.

    Examples:
        Convert 1 bigha to ropanis:
        >>> terai_to_hilly(1, 'bigha', 'ropani')
        13.31

        Convert 10 katthas to aanas:
        >>> terai_to_hilly(10, 'kattha', 'aana')
        6.23
    """
    # Convert to sq meters first
    area_m2 = terai_to_sq_meters(value, from_unit)
    # Then sq meters to the Hilly unit
    return sq_meters_to_hilly(area_m2, to_unit)


def hilly_to_terai(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert from a Hilly unit (ropani, aana, paisa, daam) to a Terai unit
    (bigha, kattha, dhur).

    Args:
        value (float): Amount in the Hilly unit.
        from_unit (str): One of 'ropani', 'aana', 'paisa', 'daam'.
        to_unit (str): One of 'bigha', 'kattha', 'dhur'.

    Returns:
        float: Converted value in the Terai unit.

    Raises:
        ValueError: If either from_unit or to_unit is not recognized.

    Examples:
        Convert 1 ropani to bighas:
        >>> hilly_to_terai(1, 'ropani', 'bigha')
        0.075

        Convert 16 daams to dhurs:
        >>> hilly_to_terai(16, 'daam', 'dhur')
        0.94
    """
    # Convert to sq meters first
    area_m2 = hilly_to_sq_meters(value, from_unit)
    # Then sq meters to the Terai unit
    return sq_meters_to_terai(area_m2, to_unit)