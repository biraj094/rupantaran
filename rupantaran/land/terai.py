"""
terai.py

Functions for converting within the Terai land measurement system
and between Terai units and square meters.
"""

from .constants import TERAI_TO_SQ_M, TERAI_CONVERSION_FACTORS

def terai_to_sq_meters(value: float, from_unit: str) -> float:
    """
    Convert a value from a Terai land unit (bigha, kattha, dhur) to square meters.

    Args:
        value (float): The numeric amount to convert.
        from_unit (str): The Terai land unit ('bigha', 'kattha', or 'dhur').

    Returns:
        float: The area in square meters.

    Raises:
        ValueError: If the from_unit is not a recognized Terai unit.

    Examples:
        Convert 2 bighas to square meters:
        >>> terai_to_sq_meters(2, 'bigha')
        13545.26

        Convert 10 katthas to square meters:
        >>> terai_to_sq_meters(10, 'kattha')
        3386.3
    """
    unit_lower = from_unit.lower()
    if unit_lower not in TERAI_TO_SQ_M:
        raise ValueError(f"Unsupported Terai unit: {from_unit}")
    return value * TERAI_TO_SQ_M[unit_lower]


def sq_meters_to_terai(area_m2: float, to_unit: str) -> float:
    """
    Convert a value in square meters to a specified Terai land unit (bigha, kattha, dhur).

    Args:
        area_m2 (float): The area in square meters.
        to_unit (str): The Terai land unit to convert to ('bigha', 'kattha', or 'dhur').

    Returns:
        float: The converted area in the specified Terai unit.

    Raises:
        ValueError: If the to_unit is not a recognized Terai unit.

    Examples:
        Convert 6772.63 square meters to bighas:
        >>> sq_meters_to_terai(6772.63, 'bigha')
        1.0

        Convert 1693 square meters to dhurs:
        >>> sq_meters_to_terai(1693, 'dhur')
        100.0
    """
    unit_lower = to_unit.lower()
    if unit_lower not in TERAI_TO_SQ_M:
        raise ValueError(f"Unsupported Terai unit: {to_unit}")
    return area_m2 / TERAI_TO_SQ_M[unit_lower]


def terai_to_terai(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert directly between any two Terai land units (bigha, kattha, dhur) using direct conversion factors.

    Args:
        value (float): The numeric amount in the from_unit.
        from_unit (str): The source Terai land unit ('bigha', 'kattha', or 'dhur').
        to_unit (str): The target Terai land unit ('bigha', 'kattha', or 'dhur').

    Returns:
        float: The converted value in the target Terai unit.

    Raises:
        ValueError: If the from_unit or to_unit is not a recognized Terai unit.
    """
    if from_unit not in TERAI_CONVERSION_FACTORS or to_unit not in TERAI_CONVERSION_FACTORS[from_unit]:
        raise ValueError("Invalid Terai land unit provided.")
    
    return value * TERAI_CONVERSION_FACTORS[from_unit][to_unit]
