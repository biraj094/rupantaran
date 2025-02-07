import pytest
import rupantaran.land.terai as terai


def test_terai_to_sq_meters():
    assert terai.terai_to_sq_meters(1, "bigha") == pytest.approx(6772.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "kattha") == pytest.approx(338.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "dhur") == pytest.approx(16.93, rel=1e-2)


def test_sq_meters_to_terai():
    assert terai.sq_meters_to_terai(6772.63, "bigha") == pytest.approx(1.0, rel=1e-2)
    assert terai.sq_meters_to_terai(338.63, "kattha") == pytest.approx(1.0, rel=1e-2)


def test_terai_to_terai():
    assert terai.terai_to_terai(1, "bigha", "kattha") == pytest.approx(20, rel=1e-2)
    assert terai.terai_to_terai(20, "kattha", "bigha") == pytest.approx(1, rel=1e-2)
