"""
terai.py

Functions for converting within the Terai land measurement system
and between Terai units and square meters, with configurable floating point precision.
"""

from .constants import TERAI_TO_SQ_M, TERAI_CONVERSION_FACTORS

def terai_to_sq_meters(value: float, from_unit: str, precision: int = 4) -> float:
    """
    Convert a value from a Terai land unit (bigha, kattha, dhur) to square meters.

    Args:
        value (float): The numeric amount to convert.
        from_unit (str): The Terai land unit ('bigha', 'kattha', or 'dhur').
        precision (int, optional): Number of decimal places to round to. Default is 4.

    Returns:
        float: The area in square meters, rounded to the specified precision.

    Raises:
        ValueError: If the from_unit is not a recognized Terai unit or value is not numeric.
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    
    unit_lower = from_unit.lower()
    if unit_lower not in TERAI_TO_SQ_M:
        raise ValueError(f"Unsupported Terai unit: {from_unit}")
    
    return round(value * TERAI_TO_SQ_M[unit_lower], precision)

def sq_meters_to_terai(area_m2: float, to_unit: str, precision: int = 4) -> float:
    """
    Convert a value in square meters to a specified Terai land unit (bigha, kattha, dhur).

    Args:
        area_m2 (float): The area in square meters.
        to_unit (str): The Terai land unit to convert to ('bigha', 'kattha', or 'dhur').
        precision (int, optional): Number of decimal places to round to. Default is 4.

    Returns:
        float: The converted area in the specified Terai unit, rounded to the specified precision.

    Raises:
        ValueError: If the to_unit is not a recognized Terai unit or area_m2 is not numeric.
    """
    if not isinstance(area_m2, (int, float)):
        raise ValueError("Area must be a number.")
    
    unit_lower = to_unit.lower()
    if unit_lower not in TERAI_TO_SQ_M:
        raise ValueError(f"Unsupported Terai unit: {to_unit}")
    
    return round(area_m2 / TERAI_TO_SQ_M[unit_lower], precision)

def terai_to_terai(value: float, from_unit: str, to_unit: str, precision: int = 4) -> float:
    """
    Convert directly between any two Terai land units (bigha, kattha, dhur) using direct conversion factors.

    Args:
        value (float): The numeric amount in the from_unit.
        from_unit (str): The source Terai land unit ('bigha', 'kattha', or 'dhur').
        to_unit (str): The target Terai land unit ('bigha', 'kattha', or 'dhur').
        precision (int, optional): Number of decimal places to round to. Default is 4.

    Returns:
        float: The converted value in the target Terai unit, rounded to the specified precision.

    Raises:
        ValueError: If the from_unit or to_unit is not a recognized Terai unit or value is not numeric.
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    
    if from_unit not in TERAI_CONVERSION_FACTORS or to_unit not in TERAI_CONVERSION_FACTORS[from_unit]:
        raise ValueError("Invalid Terai land unit provided.")
    
    return round(value * TERAI_CONVERSION_FACTORS[from_unit][to_unit], precision)
