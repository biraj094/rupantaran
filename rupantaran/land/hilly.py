"""
hilly.py

This module provides functions to convert values between different Hilly land measurement units 
and square meters. It allows conversions with configurable floating-point precision.

Functions:
- `hilly_to_sq_meters`: Converts a value from a Hilly land unit to square meters.
- `sq_meters_to_hilly`: Converts a value in square meters to a Hilly land unit.
- `hilly_to_hilly`: Converts directly between two Hilly land units.

Constants:
- `HILLY_TO_SQ_M`: Dictionary mapping Hilly land units to their square meter equivalents.
- `HILLY_CONVERSION_FACTORS`: Nested dictionary containing direct conversion ratios between Hilly land units.
"""

from .constants import HILLY_TO_SQ_M, HILLY_CONVERSION_FACTORS


def hilly_to_sq_meters(value: float, from_unit: str, precision: int = 4) -> float:
    """
    Converts a value from a Hilly land unit to square meters.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param from_unit: The Hilly land unit (e.g., 'ropani', 'aana', 'paisa', 'dam').
    :type from_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent area in square meters, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `from_unit` is not a recognized Hilly land unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import hilly
        result = hilly.hilly_to_sq_meters(value = 5, from_unit = "ropani", precision = 2  )
        print(result) 
    """


    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    unit_lower = from_unit.lower()
    if unit_lower not in HILLY_TO_SQ_M:
        raise ValueError(f"Unsupported Hilly unit: {from_unit}")

    return round(value * HILLY_TO_SQ_M[unit_lower], precision)


def sq_meters_to_hilly(area_m2: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value in square meters to a specified Hilly land unit.

    :param area_m2: The area in square meters (must be non-negative).
    :type area_m2: float
    :param to_unit: The Hilly land unit to convert to (e.g., 'ropani', 'aana', 'paisa', 'dam').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent area in the specified Hilly land unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `area_m2` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized Hilly land unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import hilly
        result = hilly.sq_meters_to_hilly(area_m2 = 500, to_unit = "aana", precision = 2)
        print(result) 
    """

    if not isinstance(area_m2, (int, float)):
        raise ValueError("Input area must be a number.")
    if area_m2 < 0:
        raise ValueError("Input area must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    unit_lower = to_unit.lower()
    if unit_lower not in HILLY_TO_SQ_M:
        raise ValueError(f"Unsupported Hilly unit: {to_unit}")

    return round(area_m2 / HILLY_TO_SQ_M[unit_lower], precision)


def hilly_to_hilly(
    value: float, from_unit: str, to_unit: str, precision: int = 4
) -> float:
    """
    Converts directly between any two Hilly land units using predefined conversion factors.

    :param value: The numeric amount in the `from_unit` (must be non-negative).
    :type value: float
    :param from_unit: The source Hilly land unit (e.g., 'ropani', 'aana', 'paisa', 'dam').
    :type from_unit: str
    :param to_unit: The target Hilly land unit (e.g., 'ropani', 'aana', 'paisa', 'dam').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent value in the target Hilly land unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If either `from_unit` or `to_unit` is not recognized.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import hilly
        result = hilly.hilly_to_hilly(value = 10, from_unit = "aana", to_unit = "ropani", precision = 2)
        print(result) 
    """
 
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if (
        from_unit not in HILLY_CONVERSION_FACTORS
        or to_unit not in HILLY_CONVERSION_FACTORS[from_unit]
    ):
        raise ValueError("Invalid Hilly land unit provided.")

    return round(value * HILLY_CONVERSION_FACTORS[from_unit][to_unit], precision)
