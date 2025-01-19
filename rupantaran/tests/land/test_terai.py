"""
test_terai.py

Unit tests for functions in 'land/terai.py'.
"""
import pytest
from rupantaran.land.terai import terai_to_sq_meters, sq_meters_to_terai

def test_terai_to_sq_meters_bigha():
    assert terai_to_sq_meters(1, "bigha") == pytest.approx(6772.63, 0.1)

def test_sq_meters_to_terai():
    result = sq_meters_to_terai(6772.63, "bigha")
    assert result == pytest.approx(1.0, 0.001)