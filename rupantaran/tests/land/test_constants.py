import pytest
from rupantaran.land.constants import TERAI_TO_SQ_M, HILLY_TO_SQ_M

def test_terai_constants():
    assert "bigha" in TERAI_TO_SQ_M
    assert "kattha" in TERAI_TO_SQ_M
    assert "dhur" in TERAI_TO_SQ_M
    assert TERAI_TO_SQ_M["bigha"] == pytest.approx(6772.63, rel=1e-2)
    assert TERAI_TO_SQ_M["kattha"] == pytest.approx(338.63, rel=1e-2)
    assert TERAI_TO_SQ_M["dhur"] == pytest.approx(16.93, rel=1e-2)

def test_hilly_constants():
    assert "ropani" in HILLY_TO_SQ_M
    assert "aana" in HILLY_TO_SQ_M
    assert "paisa" in HILLY_TO_SQ_M
    assert "daam" in HILLY_TO_SQ_M
    assert HILLY_TO_SQ_M["ropani"] == pytest.approx(508.74, rel=1e-2)
    assert HILLY_TO_SQ_M["aana"] == pytest.approx(31.79, rel=1e-2)
    assert HILLY_TO_SQ_M["paisa"] == pytest.approx(7.95, rel=1e-2)
    assert HILLY_TO_SQ_M["daam"] == pytest.approx(1.99, rel=1e-2)