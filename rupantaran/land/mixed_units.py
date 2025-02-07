"""
mixed_units.py

Functions for parsing "mixed" expressions (like '2 ropani 3 aana')
into square meters, and also converting square meters
back into "mixed" expressions. Includes cross-system "mixed" conversions.
"""

from .terai import terai_to_sq_meters
from .hilly import hilly_to_sq_meters
from .constants import TERAI_TO_SQ_M, HILLY_TO_SQ_M
from .terai import sq_meters_to_terai
from .hilly import sq_meters_to_hilly

def parse_terai_mixed_unit(expression: str) -> float:
    """
    Parse a mixed Terai expression (e.g. '1 bigha 5 kattha 10 dhur')
    into total square meters.

    Args:
        expression (str): A string like '1 bigha 5 kattha 10 dhur'.

    Returns:
        float: Total area in square meters.

    Raises:
        ValueError: If parsing fails or an unsupported unit is encountered.

    Examples:
        >>> parse_terai_mixed_unit('1 bigha 5 kattha 10 dhur')
        8632.08
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
        except ValueError:
            raise ValueError(f"Invalid numeric value '{val_str}' in '{expression}'")
        
        total_m2 += terai_to_sq_meters(val, unit_str)
    return total_m2

def parse_hilly_mixed_unit(expression: str) -> float:
    """
    Parse a mixed Hilly expression (e.g. '2 ropani 3 aana 2 paisa')
    into total square meters.

    Args:
        expression (str): A string like '2 ropani 3 aana 2 paisa'.

    Returns:
        float: Total area in square meters.

    Raises:
        ValueError: If parsing fails or an unsupported unit is encountered.

    Examples:
        >>> parse_hilly_mixed_unit('2 ropani 3 aana 2 paisa')
        1082.55
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
        except ValueError:
            raise ValueError(f"Invalid numeric value '{val_str}' in '{expression}'")

        total_m2 += hilly_to_sq_meters(val, unit_str)
    return total_m2

def sq_meters_to_terai_mixed(area_m2: float, precision: int = 4) -> str:
    """
    Convert an area in square meters into a 'mixed' Terai format:
    e.g. 'X bigha Y kattha Z dhur'.

    Args:
        area_m2 (float): Area in square meters.
        precision (int, optional): Floating point precision for dhur. Defaults to 4.

    Returns:
        str: Formatted string in bigha/kattha/dhur.

    Examples:
        >>> sq_meters_to_terai_mixed(8632.08)
        '1 bigha 5 kattha 10.0000 dhur'
    """
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
    Convert a Hilly mixed expression into a Terai mixed expression.

    Args:
        expression (str): A Hilly mixed string.
        precision (int, optional): Floating point precision for dhur. Defaults to 4.

    Returns:
        str: A Terai mixed string.

    Examples:
        >>> hilly_mixed_to_terai_mixed('2 ropani 3 aana 2 paisa')
        '0 bigha 2 kattha 3.5520 dhur'
    """
    area_m2 = parse_hilly_mixed_unit(expression)
    return sq_meters_to_terai_mixed(area_m2, precision)
