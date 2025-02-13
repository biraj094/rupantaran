"""
terai.py

This module provides functions to convert values between different Terai land measurement units 
(bigha, kattha, dhur) and square meters. The conversions ensure precision and support configurable 
floating-point rounding.

Functions:
- `terai_to_sq_meters`: Converts a value from a Terai land unit to square meters.
- `sq_meters_to_terai`: Converts a value in square meters to a Terai land unit.
- `terai_to_terai`: Converts directly between two Terai land units.

Constants:
- `TERAI_TO_SQ_M`: Dictionary mapping Terai land units to their square meter equivalents.
- `TERAI_CONVERSION_FACTORS`: Nested dictionary containing direct conversion ratios between Terai land units.
"""

from .constants import TERAI_TO_SQ_M, TERAI_CONVERSION_FACTORS


def terai_to_sq_meters(value: float, from_unit: str, precision: int = 4) -> float:
    """
    Converts a value from a Terai land unit (bigha, kattha, dhur) to square meters.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param from_unit: The Terai land unit ('bigha', 'kattha', or 'dhur').
    :type from_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent area in square meters, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `from_unit` is not a recognized Terai land unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import terai
        result = terai.terai_to_sq_meters(value = 2, from_unit = "bigha", precision = 2)
        print(result)
    """

    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    unit_lower = from_unit.lower()
    if unit_lower not in TERAI_TO_SQ_M:
        raise ValueError(f"Unsupported Terai unit: {from_unit}")

    return round(value * TERAI_TO_SQ_M[unit_lower], precision)


def sq_meters_to_terai(area_m2: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value in square meters to a specified Terai land unit.

    :param area_m2: The area in square meters (must be non-negative).
    :type area_m2: float
    :param to_unit: The Terai land unit to convert to ('bigha', 'kattha', or 'dhur').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent area in the specified Terai land unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `area_m2` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized Terai land unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import terai
        result = terai.sq_meters_to_terai(area_m2 = 500, to_unit = "kattha", precision = 2)
        print(result) 
    """
    if not isinstance(area_m2, (int, float)):
        raise ValueError("Area must be a number.")
    if area_m2 < 0:
        raise ValueError("Input area must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    unit_lower = to_unit.lower()
    if unit_lower not in TERAI_TO_SQ_M:
        raise ValueError(f"Unsupported Terai unit: {to_unit}")

    return round(area_m2 / TERAI_TO_SQ_M[unit_lower], precision)


def terai_to_terai(value: float, from_unit: str, to_unit: str, precision: int = 4) -> float:
    """
    Converts directly between any two Terai land units using predefined conversion factors.

    :param value: The numeric amount in the `from_unit` (must be non-negative).
    :type value: float
    :param from_unit: The source Terai land unit ('bigha', 'kattha', or 'dhur').
    :type from_unit: str
    :param to_unit: The target Terai land unit ('bigha', 'kattha', or 'dhur').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent value in the target Terai land unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If either `from_unit` or `to_unit` is not recognized.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import terai
        result = terai.terai_to_terai(value = 3, from_unit = "bigha", to_unit = "kattha", precision = 2)
        print(result) 
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if (from_unit not in TERAI_CONVERSION_FACTORS 
        or to_unit not in TERAI_CONVERSION_FACTORS[from_unit]):
        raise ValueError("Invalid Terai land unit provided.")

    return round(value * TERAI_CONVERSION_FACTORS[from_unit][to_unit], precision)
