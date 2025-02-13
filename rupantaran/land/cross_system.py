"""
cross_system.py

This module provides functions to convert land measurements between Terai and Hilly land units 
by using square meters as an intermediary conversion step.

Functions:
- `terai_to_hilly`: Converts a value from a Terai land unit to a Hilly land unit.
- `hilly_to_terai`: Converts a value from a Hilly land unit to a Terai land unit.

Dependencies:
- `terai_to_sq_meters`: Converts Terai land units to square meters.
- `sq_meters_to_terai`: Converts square meters to Terai land units.
- `hilly_to_sq_meters`: Converts Hilly land units to square meters.
- `sq_meters_to_hilly`: Converts square meters to Hilly land units.
"""
from .terai import terai_to_sq_meters, sq_meters_to_terai
from .hilly import hilly_to_sq_meters, sq_meters_to_hilly


def terai_to_hilly(value: float, from_unit: str, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from a Terai land unit to a Hilly land unit using square meters as an intermediary.

    :param value: The numeric amount in the `from_unit` (must be non-negative).
    :type value: float
    :param from_unit: The source Terai land unit (e.g., 'bigha', 'kattha', 'dhur').
    :type from_unit: str
    :param to_unit: The target Hilly land unit (e.g., 'ropani', 'aana', 'paisa', 'daam').
    :type to_unit: str
    :param precision: Number of decimal places for rounding (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: The equivalent value in the target Hilly land unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `from_unit` is not a recognized Terai land unit.
        - If `to_unit` is not a recognized Hilly land unit.


    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import cross_system
        result = cross_system.terai_to_hilly(value = 1, from_unit = "bigha", to_unit = "ropani", precision = 2)
        print(result) 
    """

    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    # Convert to square meters first
    area_m2 = terai_to_sq_meters(value, from_unit)
    # Convert square meters to the Hilly unit
    return round(sq_meters_to_hilly(area_m2, to_unit), precision)


def hilly_to_terai(value: float, from_unit: str, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from a Hilly land unit to a Terai land unit using square meters as an intermediary.

    :param value: The numeric amount in the `from_unit` (must be non-negative).
    :type value: float
    :param from_unit: The source Hilly land unit (e.g., 'ropani', 'aana', 'paisa', 'daam').
    :type from_unit: str
    :param to_unit: The target Terai land unit (e.g., 'bigha', 'kattha', 'dhur').
    :type to_unit: str
    :param precision: Number of decimal places for rounding (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: The equivalent value in the target Terai land unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `from_unit` is not a recognized Hilly land unit.
        - If `to_unit` is not a recognized Terai land unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import cross_system
        result = cross_system.hilly_to_terai(value = 1, from_unit = "ropani", to_unit = "bigha", precision = 2)
        print(result) 
    """

    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")
    if value < 0:
        raise ValueError("Input value must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    # Convert to square meters first
    area_m2 = hilly_to_sq_meters(value, from_unit)
    # Convert square meters to the Terai unit
    return round(sq_meters_to_terai(area_m2, to_unit), precision)
