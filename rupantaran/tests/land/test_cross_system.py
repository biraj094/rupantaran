import pytest
import rupantaran.land.cross_system as cross_system

def test_hilly_to_terai():
    result = cross_system.hilly_to_terai(1, "ropani", "kattha")
    assert isinstance(result, float)

def test_terai_to_hilly():
    result = cross_system.terai_to_hilly(1, "bigha", "ropani")
    assert isinstance(result, float)