import pytest
import rupantaran.land.hilly as hilly

def test_hilly_to_sq_meters():
    assert hilly.hilly_to_sq_meters(1, "ropani") == pytest.approx(508.74, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "aana") == pytest.approx(31.79, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "paisa") == pytest.approx(7.95, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "daam") == pytest.approx(1.99, rel=1e-2)

def test_sq_meters_to_hilly():
    assert hilly.sq_meters_to_hilly(508.74, "ropani") == pytest.approx(1.0, rel=1e-2)
    assert hilly.sq_meters_to_hilly(31.79, "aana") == pytest.approx(1.0, rel=1e-2)

def test_hilly_to_hilly():
    assert hilly.hilly_to_hilly(1, "ropani", "aana") == pytest.approx(16, rel=1e-2)
    assert hilly.hilly_to_hilly(16, "aana", "ropani") == pytest.approx(1, rel=1e-2)