"""
mixed_units.py

This module provides functions for parsing and converting mixed land measurement expressions 
(e.g., '2 ropani 3 aana') into square meters and vice versa. It also supports cross-system 
conversions between Hilly and Terai land measurement systems.

Functions:
- `parse_terai_mixed_unit`: Parses a Terai mixed-unit expression into square meters.
- `parse_hilly_mixed_unit`: Parses a Hilly mixed-unit expression into square meters.
- `sq_meters_to_terai_mixed`: Converts square meters to a Terai mixed-unit expression.
- `sq_meters_to_hilly_mixed`: Converts square meters to a Hilly mixed-unit expression.
- `hilly_mixed_to_terai_mixed`: Converts a Hilly mixed-unit expression to a Terai mixed-unit expression.
- `terai_mixed_to_hilly_mixed`: Converts a Terai mixed-unit expression to a Hilly mixed-unit expression.

Constants:
- `TERAI_TO_SQ_M`: Dictionary mapping Terai land units to their square meter equivalents.
- `HILLY_TO_SQ_M`: Dictionary mapping Hilly land units to their square meter equivalents.
"""

from .terai import terai_to_sq_meters
from .hilly import hilly_to_sq_meters
from .constants import TERAI_TO_SQ_M, HILLY_TO_SQ_M


def parse_terai_mixed_unit(expression: str) -> float:
    """
    Parses a mixed Terai land measurement expression into total square meters.

    :param expression: A string representing a Terai mixed-unit value (e.g., '1 bigha 5 kattha 10 dhur').
    :type expression: str
    :return: The equivalent area in square meters.
    :rtype: float

    :raises ValueError:
        - If the input string format is incorrect.
        - If an unsupported unit is encountered.
        - If any value in the expression is negative.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import mixed_units
        result = mixed_units.parse_terai_mixed_unit(expression = "1 bigha 5 kattha 10 dhur")
        print(result) 
    """
    parts = expression.lower().split()
    if len(parts) % 2 != 0:
        raise ValueError("Terai mixed-unit string must have pairs of (value, unit).")

    total_m2 = 0.0
    for i in range(0, len(parts), 2):
        val_str = parts[i]
        unit_str = parts[i + 1]
        try:
            val = float(val_str)
            if val < 0:
                raise ValueError("Input value must be non-negative.")
        except ValueError as e:
            if "non-negative" in str(e):
                raise
            raise ValueError(f"Invalid numeric value '{val_str}' in '{expression}'")

        total_m2 += terai_to_sq_meters(val, unit_str)
    return total_m2


def parse_hilly_mixed_unit(expression: str) -> float:
    """
    Parses a mixed Hilly land measurement expression into total square meters.

    :param expression: A string representing a Hilly mixed-unit value (e.g., '2 ropani 3 aana 2 paisa').
    :type expression: str
    :return: The equivalent area in square meters.
    :rtype: float

    :raises ValueError:
        - If the input string format is incorrect.
        - If an unsupported unit is encountered.
        - If any value in the expression is negative.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import mixed_units
        result = mixed_units.parse_hilly_mixed_unit(expression = "2 ropani 3 aana 2 paisa")
        print(result) 
    """

    parts = expression.lower().split()
    if len(parts) % 2 != 0:
        raise ValueError("Hilly mixed-unit string must have pairs of (value, unit).")

    total_m2 = 0.0
    for i in range(0, len(parts), 2):
        val_str = parts[i]
        unit_str = parts[i + 1]
        try:
            val = float(val_str)
            if val < 0:
                raise ValueError("Input value must be non-negative.")
        except ValueError as e:
            if "non-negative" in str(e):
                raise
            raise ValueError(f"Invalid numeric value '{val_str}' in '{expression}'")

        total_m2 += hilly_to_sq_meters(val, unit_str)
    return total_m2


def sq_meters_to_terai_mixed(area_m2: float, precision: int = 4) -> str:
    """
    Converts a given area in square meters to a Terai mixed-unit expression.

    :param area_m2: The area in square meters (must be non-negative).
    :type area_m2: float
    :param precision: Number of decimal places for dhur rounding (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: The equivalent Terai mixed-unit expression.
    :rtype: str

    :raises ValueError:
        - If `area_m2` is negative or not a number.
        - If `precision` is negative.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import mixed_units
        result = mixed_units.sq_meters_to_terai_mixed(area_m2 = 500, precision = 2)
        print(result) 
    """
    if not isinstance(area_m2, (int, float)):
        raise ValueError("Input area must be a number.")
    if area_m2 < 0:
        raise ValueError("Input area must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    BIGHA_M2 = TERAI_TO_SQ_M["bigha"]
    KATTHA_M2 = TERAI_TO_SQ_M["kattha"]
    DHUR_M2 = TERAI_TO_SQ_M["dhur"]

    bigha = int(area_m2 // BIGHA_M2)
    remainder = area_m2 % BIGHA_M2

    kattha = int(remainder // KATTHA_M2)
    remainder = remainder % KATTHA_M2

    dhur = round(remainder / DHUR_M2, precision)

    return f"{bigha} bigha {kattha} kattha {dhur:.{precision}f} dhur"


def hilly_mixed_to_terai_mixed(expression: str, precision: int = 4) -> str:
    """
    Converts a Hilly mixed-unit expression to a Terai mixed-unit expression.

    :param expression: A string representing a Hilly mixed-unit value.
    :type expression: str
    :param precision: Number of decimal places for dhur rounding (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: The equivalent Terai mixed-unit expression.
    :rtype: str

    :raises ValueError:
        - If the input string format is incorrect.
        - If precision is negative.


    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import mixed_units
        result = mixed_units.hilly_mixed_to_terai_mixed(expression = "2 ropani 3 aana 2 paisa", precision = 2)
        print(result) 
    """
    if precision < 0:
        raise ValueError("Precision must be non-negative.")
    area_m2 = parse_hilly_mixed_unit(expression)
    return sq_meters_to_terai_mixed(area_m2, precision)


def sq_meters_to_hilly_mixed(area_m2: float, precision: int = 4) -> str:
    """
    Converts a given area in square meters to a Hilly mixed-unit expression.

    :param area_m2: The area in square meters (must be non-negative).
    :type area_m2: float
    :param precision: Number of decimal places for daam rounding (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: The equivalent Hilly mixed-unit expression.
    :rtype: str

    :raises ValueError:
        - If `area_m2` is negative or not a number.
        - If `precision` is negative.
 

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import mixed_units
        result = mixed_units.sq_meters_to_hilly_mixed(area_m2 = 500, precision = 2)
        print(result) 
    """
    if not isinstance(area_m2, (int, float)):
        raise ValueError("Input area must be a number.")
    if area_m2 < 0:
        raise ValueError("Input area must be non-negative.")
    if precision < 0:
        raise ValueError("Precision must be non-negative.")

    ROPANI_M2 = HILLY_TO_SQ_M["ropani"]
    AANA_M2 = HILLY_TO_SQ_M["aana"]
    PAISA_M2 = HILLY_TO_SQ_M["paisa"]
    DAAM_M2 = HILLY_TO_SQ_M["daam"]

    ropani = int(area_m2 // ROPANI_M2)
    remainder = area_m2 % ROPANI_M2

    aana = int(remainder // AANA_M2)
    remainder = remainder % AANA_M2

    paisa = int(remainder // PAISA_M2)
    remainder = remainder % PAISA_M2

    daam = round(remainder / DAAM_M2, precision)

    return f"{ropani} ropani {aana} aana {paisa} paisa {daam:.{precision}f} daam"


def terai_mixed_to_hilly_mixed(expression: str, precision: int = 4) -> str:

    """
    Converts a Terai mixed-unit expression to a Hilly mixed-unit expression.

    :param expression: A string representing a Terai mixed-unit value.
    :type expression: str
    :param precision: Number of decimal places for daam rounding (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: The equivalent Hilly mixed-unit expression.
    :rtype: str

    :raises ValueError:
        - If the input string format is incorrect.
        - If precision is negative.


    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.land import mixed_units
        result = mixed_units.terai_mixed_to_hilly_mixed(expression = "1 bigha 5 kattha 10 dhur", precision = 2)
        print(result) 
    """
    if precision < 0:
        raise ValueError("Precision must be non-negative.")
    area_m2 = parse_terai_mixed_unit(expression)
    return sq_meters_to_hilly_mixed(area_m2, precision)
