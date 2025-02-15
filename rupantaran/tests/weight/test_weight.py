import pytest
import random
from rupantaran.weight import (
    from_kg, from_g, from_lb, from_oz, 
    from_lal, from_tola, from_chatak, 
    from_pau, from_dharni, from_sher
)
from rupantaran.weight.constants import (
    LAL_TO, TOLA_TO, CHATAK_TO, PAU_TO, DHARNI_TO, 
    SHER_TO, KG_TO, G_TO, LB_TO, OZ_TO
)

WEIGHT_UNITS = ["lal","tola","chatak","pau","dharni","sher","kg","g","lb","oz"]

# Function to get a different unit
def get_different_unit(source_unit):
    """Returns a unit different from the source unit."""
    available_units = [unit for unit in WEIGHT_UNITS if unit != source_unit]
    return random.choice(available_units)

# Conversion functions to test
CONVERSION_FUNCTIONS = [
    (from_lal, "lal"),
    (from_tola, "tola"),
    (from_chatak, "chatak"),
    (from_pau, "pau"),
    (from_dharni, "dharni"),
    (from_sher, "sher"),
    (from_kg, "kg"),
    (from_g, "g"),
    (from_lb, "lb"),
    (from_oz, "oz"),
]
# Parameterized testing ~ Basic sanity checks for all other conversion functions 
# Runs the same test for all the conversion functions
# 10 conversion functions, 4 test methods for each function
# 1 more test_specific_conversions() for spot checks
@pytest.mark.parametrize("func,source_unit", CONVERSION_FUNCTIONS)
class TestWeightConversions:
    def test_zero_handling(self, func, source_unit):
        """Test that all functions handle zero correctly"""
        to_unit = get_different_unit(source_unit)
        assert func(0, to_unit) == 0

    def test_positive_conversion(self, func, source_unit):
        """Test that all functions can convert positive numbers"""
        to_unit = get_different_unit(source_unit)
        result = func(1.0, to_unit)
        assert isinstance(result, float)
        assert result >= 0

    def test_error_handling(self, func, source_unit):
        """Test that all functions handle errors consistently"""
        to_unit = get_different_unit(source_unit)

        with pytest.raises(ValueError):
            func(-1, to_unit)  # Negative value
        with pytest.raises(ValueError):
            func(1, "invalid_unit")  # Invalid unit
        with pytest.raises(ValueError):
            func(1, source_unit)  # Same unit as source

    def test_precision_handling(self, func, source_unit):
        """Test that all functions handle precision correctly"""
        to_unit = get_different_unit(source_unit)
        result = func(1, to_unit, precision=2)
        str_result = str(result)
        if '.' in str_result:
            assert len(str_result.split('.')[-1]) <= 2

# Test specific conversion values
def test_specific_conversions():
    """Test specific known conversion values"""
    test_cases = [
        (from_chatak, 1, "kg", 0.05831),
        (from_dharni, 1, "g", 2390.00000),
        (from_pau, 1, "oz", 7.02047),
        (from_tola, 1, "g", 11.66000),
        (from_lal, 1, "oz", 0.00411),
        (from_kg, 1, "lb", 2.20462),
        (from_g, 1000, "oz", 35.27396),
        (from_lb, 1, "g", 453.59237),
        (from_oz, 16, "g", 453.59237),
        (from_sher, 1, "lb", 1.75),
        (from_lal, 5, "g", 0.583),
        (from_tola, 10, "kg", 0.1166),
        (from_chatak, 2, "lb", 0.2571),
        (from_pau, 3, "kg", 0.597),
        (from_dharni, 4, "oz", 337.2194),
        (from_sher, 7, "g", 5572.00),
        (from_oz, 32, "kg", 0.90718),
        (from_g, 500, "lb", 1.1023),
        (from_lb, 3, "oz", 48),
        (from_kg, 2, "dharni", 0.838),
    ]
    
    for func, input_val, unit, expected in test_cases:
        result = func(input_val, unit, precision=3)  # Set fixed precision for all tests
        assert result == pytest.approx(expected, rel=1e-1), \
            f"\nFunction: {func.__name__}\nInput: {input_val} {unit}\nExpected: {expected}\nGot: {result}"

def test_conversion_constants_consistency():
    """Test that conversion constants are consistent across dictionaries"""
    # Dictionary mapping unit names to their conversion dictionaries
    conversion_dicts = {
        "lal": LAL_TO,
        "tola": TOLA_TO,
        "chatak": CHATAK_TO,
        "pau": PAU_TO,
        "dharni": DHARNI_TO,
        "sher": SHER_TO,
        "kg": KG_TO,
        "g": G_TO,
        "lb": LB_TO,
        "oz": OZ_TO
    }
    
    # Test bidirectional consistency for each pair of units
    for unit1, dict1 in conversion_dicts.items():
        for unit2, forward_value in dict1.items():
            # Get the reverse conversion value
            reverse_value = conversion_dicts[unit2][unit1]
            
            # The product of forward and reverse conversions should be approximately 1
            product = forward_value * reverse_value
            assert 0.85 <= product <= 1.15, \
                f"Inconsistent conversion between {unit1} and {unit2}: " \
                f"{unit1}->{unit2}={forward_value}, {unit2}->{unit1}={reverse_value}, " \
                f"product={product} (should be between 0.85 and 1.15)"
