"""
test_cross_system.py

Unit tests for cross-system conversions in 'land/cross_system.py'.
"""
import pytest
from rupantaran.land.cross_system import terai_to_hilly, hilly_to_terai

def test_terai_to_hilly_bigha_to_ropani():
    # 1 bigha => approx 13.3 ropani
    ropani = terai_to_hilly(1, "bigha", "ropani")
    assert ropani == pytest.approx(13.3, 0.2)