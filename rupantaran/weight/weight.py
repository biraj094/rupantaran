from functools import wraps
from typing import Callable
from .constants import (LAL_TO, TOLA_TO, CHATAK_TO, PAU_TO, DHARNI_TO, 
                       SHER_TO, KG_TO, G_TO, LB_TO, OZ_TO)

def weight_converter(conversion_map: dict) -> Callable:
    """Decorator that creates a weight conversion function using the provided conversion map."""
    def decorator(func: Callable) -> Callable:
        # @wraps(func) keeps the function’s original name and docstring intact.
        @wraps(func)
        def wrapper(value: float, to_unit: str, precision: int = 4) -> float:
            if not isinstance(value, (int, float)):
                raise ValueError("Input value must be a number.")
            if value < 0:
                raise ValueError("Input value must be non-negative.")
            if precision < 0:
                raise ValueError("Precision must be non-negative.")
            
            to_unit_lower = to_unit.lower()
            if to_unit_lower not in conversion_map:
                raise ValueError(f"Unsupported unit: {to_unit}")
            
            result = value * conversion_map[to_unit_lower]
            return round(result, precision)
        return wrapper
    return decorator

@weight_converter(LAL_TO)
def from_lal(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from lal to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'tola', 'chatak', 'pau', 'dharni', 'sher', 'kg', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_lal
        result = from_lal(value=5, to_unit="tola", precision=2)
        print(result)
    """
    pass

@weight_converter(TOLA_TO)
def from_tola(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from tola to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'chatak', 'pau', 'dharni', 'sher', 'kg', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_tola
        result = from_tola(value=5, to_unit="kg", precision=2)
        print(result)
    """
    pass

@weight_converter(CHATAK_TO)
def from_chatak(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from chatak to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'tola', 'pau', 'dharni', 'sher', 'kg', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button
hy to
        from rupantaran.weight import from_chatak
        result = from_chatak(value=5, to_unit="kg", precision=2)
        print(result)
    """
    pass

@weight_converter(PAU_TO)
def from_pau(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from pau to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'chatak', 'tola', 'dharni', 'sher', 'kg', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_pau
        result = from_pau(value=5, to_unit="kg", precision=2)
        print(result)
    """
    pass

@weight_converter(DHARNI_TO)
def from_dharni(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from dharni to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'chatak','tola', 'pau', 'sher', 'kg', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_dharni
        result = from_dharni(value=5, to_unit="kg", precision=2)
        print(result)
    """
    pass

@weight_converter(SHER_TO)
def from_sher(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from sher to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'chatak','tola', 'pau', 'dharni', 'kg', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_sher
        result = from_sher(value=5, to_unit="kg", precision=2)
        print(result)
    """
    pass

@weight_converter(KG_TO)
def from_kg(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from kilograms to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'tola', 'chatak', 'pau', 'dharni', 'sher', 'g', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_kg
        result = from_kg(value=5, to_unit="lb", precision=2)
        print(result)
    """
    pass

@weight_converter(G_TO)
def from_g(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from grams to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'tola', 'chatak', 'pau', 'dharni', 'sher', 'kg', 'lb', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_g
        result = from_g(value=5, to_unit="lb", precision=2)
        print(result)
    """
    pass

@weight_converter(LB_TO)
def from_lb(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from pounds to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'tola', 'chatak', 'pau', 'dharni', 'sher', 'g', 'kg', 'oz').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_lb
        result = from_lb(value=5, to_unit="lb", precision=2)
        print(result)
    """
    pass

@weight_converter(OZ_TO)
def from_oz(value: float, to_unit: str, precision: int = 4) -> float:
    """
    Converts a value from ounces to other weight units.

    :param value: The numeric amount to convert (must be non-negative).
    :type value: float
    :param to_unit: The target weight unit (e.g., 'lal', 'tola', 'chatak', 'pau', 'dharni', 'sher', 'g', 'lb', 'kg').
    :type to_unit: str
    :param precision: Number of decimal places to round to (must be non-negative). Default is 4.
    :type precision: int, optional
    :return: Equivalent weight in the target unit, rounded to the specified precision.
    :rtype: float

    :raises ValueError:
        - If `value` is negative or not a number.
        - If `precision` is negative.
        - If `to_unit` is not a recognized weight unit.

    .. code-block:: python
        :caption: Example
        :class: copy-button

        from rupantaran.weight import from_oz
        result = from_oz(value=5, to_unit="lb", precision=2)
        print(result)
    """
    pass
