"""
test_constants.py

Basic tests for 'land/constants.py'.
"""
import pytest
from rupantaran.land.constants import TERAI_TO_SQ_M, HILLY_TO_SQ_M


def test_terai_constants():
    assert "bigha" in TERAI_TO_SQ_M
    assert "kattha" in TERAI_TO_SQ_M
    assert "dhur" in TERAI_TO_SQ_M
    # etc.

def test_hilly_constants():
    assert "ropani" in HILLY_TO_SQ_M
    assert "aana" in HILLY_TO_SQ_M
    # etc.