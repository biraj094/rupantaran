import pytest
import rupantaran.land.terai as terai


def test_terai_to_sq_meters():
    # Basic conversions
    assert terai.terai_to_sq_meters(1, "bigha") == pytest.approx(6772.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "kattha") == pytest.approx(338.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "dhur") == pytest.approx(16.93, rel=1e-2)
    
    # Multiple values
    assert terai.terai_to_sq_meters(2.5, "bigha") == pytest.approx(16931.575, rel=1e-2)
    assert terai.terai_to_sq_meters(3.75, "kattha") == pytest.approx(1269.86, rel=1e-2)
    assert terai.terai_to_sq_meters(5.5, "dhur") == pytest.approx(93.115, rel=1e-2)
    
    # Zero values
    assert terai.terai_to_sq_meters(0, "bigha") == 0
    assert terai.terai_to_sq_meters(0, "kattha") == 0
    assert terai.terai_to_sq_meters(0, "dhur") == 0
    
    # Different precision
    assert terai.terai_to_sq_meters(1, "bigha", precision=2) == pytest.approx(6772.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "kattha", precision=1) == pytest.approx(338.6, rel=1e-1)
    assert terai.terai_to_sq_meters(1, "dhur", precision=3) == pytest.approx(16.930, rel=1e-3)
    
    # Test case sensitivity
    assert terai.terai_to_sq_meters(1, "BIGHA") == pytest.approx(6772.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "Kattha") == pytest.approx(338.63, rel=1e-2)
    assert terai.terai_to_sq_meters(1, "dHuR") == pytest.approx(16.93, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        terai.terai_to_sq_meters(1, "invalid_unit")
    with pytest.raises(ValueError):
        terai.terai_to_sq_meters("1", "bigha")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        terai.terai_to_sq_meters(-2, "kattha")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        terai.terai_to_sq_meters(1, "bigha", precision=-1)


def test_sq_meters_to_terai():
    # Basic conversions
    assert terai.sq_meters_to_terai(6772.63, "bigha") == pytest.approx(1.0, rel=1e-2)
    assert terai.sq_meters_to_terai(338.63, "kattha") == pytest.approx(1.0, rel=1e-2)
    assert terai.sq_meters_to_terai(16.93, "dhur") == pytest.approx(1.0, rel=1e-2)
    
    # Multiple values
    assert terai.sq_meters_to_terai(16931.575, "bigha") == pytest.approx(2.5, rel=1e-2)
    assert terai.sq_meters_to_terai(1269.86, "kattha") == pytest.approx(3.75, rel=1e-2)
    assert terai.sq_meters_to_terai(93.115, "dhur") == pytest.approx(5.5, rel=1e-2)
    
    # Zero values
    assert terai.sq_meters_to_terai(0, "bigha") == 0
    assert terai.sq_meters_to_terai(0, "kattha") == 0
    assert terai.sq_meters_to_terai(0, "dhur") == 0
    
    # Different precision
    assert terai.sq_meters_to_terai(6772.63, "bigha", precision=2) == pytest.approx(1.00, rel=1e-2)
    assert terai.sq_meters_to_terai(338.63, "kattha", precision=1) == pytest.approx(1.0, rel=1e-1)
    assert terai.sq_meters_to_terai(16.93, "dhur", precision=3) == pytest.approx(1.000, rel=1e-3)
    
    # Test case sensitivity
    assert terai.sq_meters_to_terai(6772.63, "BIGHA") == pytest.approx(1.0, rel=1e-2)
    assert terai.sq_meters_to_terai(338.63, "Kattha") == pytest.approx(1.0, rel=1e-2)
    assert terai.sq_meters_to_terai(16.93, "dHuR") == pytest.approx(1.0, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        terai.sq_meters_to_terai(100, "invalid_unit")
    with pytest.raises(ValueError):
        terai.sq_meters_to_terai("100", "bigha")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input area must be non-negative"):
        terai.sq_meters_to_terai(-6772.63, "bigha")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        terai.sq_meters_to_terai(6772.63, "bigha", precision=-1)


def test_terai_to_terai():
    # Basic conversions
    assert terai.terai_to_terai(1, "bigha", "kattha") == pytest.approx(20, rel=1e-2)
    assert terai.terai_to_terai(1, "bigha", "dhur") == pytest.approx(400, rel=1e-2)
    assert terai.terai_to_terai(1, "kattha", "dhur") == pytest.approx(20, rel=1e-2)
    
    # Reverse conversions
    assert terai.terai_to_terai(20, "kattha", "bigha") == pytest.approx(1, rel=1e-2)
    assert terai.terai_to_terai(400, "dhur", "bigha") == pytest.approx(1, rel=1e-2)
    assert terai.terai_to_terai(20, "dhur", "kattha") == pytest.approx(1, rel=1e-2)
    
    # Multiple values
    assert terai.terai_to_terai(2.5, "bigha", "kattha") == pytest.approx(50, rel=1e-2)
    assert terai.terai_to_terai(3.75, "kattha", "dhur") == pytest.approx(75, rel=1e-2)
    
    # Zero values
    assert terai.terai_to_terai(0, "bigha", "kattha") == 0
    assert terai.terai_to_terai(0, "kattha", "dhur") == 0
    
    # Different precision
    assert terai.terai_to_terai(1, "bigha", "kattha", precision=2) == pytest.approx(20.00, rel=1e-2)
    assert terai.terai_to_terai(1, "kattha", "dhur", precision=1) == pytest.approx(20.0, rel=1e-1)
    
    # Test case sensitivity
    assert terai.terai_to_terai(1, "BIGHA", "KATTHA") == pytest.approx(20, rel=1e-2)
    assert terai.terai_to_terai(1, "Kattha", "Dhur") == pytest.approx(20, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        terai.terai_to_terai(1, "invalid_unit", "bigha")
    with pytest.raises(ValueError):
        terai.terai_to_terai(1, "bigha", "invalid_unit")
    with pytest.raises(ValueError):
        terai.terai_to_terai("1", "bigha", "kattha")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        terai.terai_to_terai(-2, "bigha", "kattha")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        terai.terai_to_terai(1, "bigha", "kattha", precision=-1)
