import pytest
import rupantaran.land.hilly as hilly


def test_hilly_to_sq_meters():
    # Basic conversions
    assert hilly.hilly_to_sq_meters(1, "ropani") == pytest.approx(508.74, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "aana") == pytest.approx(31.79, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "paisa") == pytest.approx(7.95, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "daam") == pytest.approx(1.99, rel=1e-2)
    
    # Multiple values
    assert hilly.hilly_to_sq_meters(2.5, "ropani") == pytest.approx(1271.85, rel=1e-2)
    assert hilly.hilly_to_sq_meters(3.75, "aana") == pytest.approx(119.21, rel=1e-2)
    
    # Zero values
    assert hilly.hilly_to_sq_meters(0, "ropani") == 0
    assert hilly.hilly_to_sq_meters(0, "aana") == 0
    
    # Different precision
    assert hilly.hilly_to_sq_meters(1, "ropani", precision=2) == pytest.approx(508.74, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "aana", precision=1) == pytest.approx(31.8, rel=1e-1)
    
    # Test case sensitivity
    assert hilly.hilly_to_sq_meters(1, "ROPANI") == pytest.approx(508.74, rel=1e-2)
    assert hilly.hilly_to_sq_meters(1, "Aana") == pytest.approx(31.79, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        hilly.hilly_to_sq_meters(1, "invalid_unit")
    with pytest.raises(ValueError):
        hilly.hilly_to_sq_meters("1", "ropani")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        hilly.hilly_to_sq_meters(-2, "paisa")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        hilly.hilly_to_sq_meters(1, "ropani", precision=-1)


def test_sq_meters_to_hilly():
    # Basic conversions
    assert hilly.sq_meters_to_hilly(508.74, "ropani") == pytest.approx(1.0, rel=1e-2)
    assert hilly.sq_meters_to_hilly(31.79, "aana") == pytest.approx(1.0, rel=1e-2)
    assert hilly.sq_meters_to_hilly(7.95, "paisa") == pytest.approx(1.0, rel=1e-2)
    assert hilly.sq_meters_to_hilly(1.99, "daam") == pytest.approx(1.0, rel=1e-2)
    
    # Multiple values
    assert hilly.sq_meters_to_hilly(1271.85, "ropani") == pytest.approx(2.5, rel=1e-2)
    assert hilly.sq_meters_to_hilly(119.21, "aana") == pytest.approx(3.75, rel=1e-2)
    assert hilly.sq_meters_to_hilly(19.875, "paisa") == pytest.approx(2.5, rel=1e-2)
    
    # Zero values
    assert hilly.sq_meters_to_hilly(0, "ropani") == 0
    assert hilly.sq_meters_to_hilly(0, "aana") == 0
    assert hilly.sq_meters_to_hilly(0, "paisa") == 0
    assert hilly.sq_meters_to_hilly(0, "daam") == 0
    
    # Different precision
    assert hilly.sq_meters_to_hilly(508.74, "ropani", precision=2) == pytest.approx(1.00, rel=1e-2)
    assert hilly.sq_meters_to_hilly(31.79, "aana", precision=1) == pytest.approx(1.0, rel=1e-1)
    assert hilly.sq_meters_to_hilly(7.95, "paisa", precision=3) == pytest.approx(1.000, rel=1e-3)
    
    # Test case sensitivity
    assert hilly.sq_meters_to_hilly(508.74, "ROPANI") == pytest.approx(1.0, rel=1e-2)
    assert hilly.sq_meters_to_hilly(31.79, "Aana") == pytest.approx(1.0, rel=1e-2)
    assert hilly.sq_meters_to_hilly(7.95, "PaIsA") == pytest.approx(1.0, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        hilly.sq_meters_to_hilly(100, "invalid_unit")
    with pytest.raises(ValueError):
        hilly.sq_meters_to_hilly("100", "ropani")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input area must be non-negative"):
        hilly.sq_meters_to_hilly(-508.74, "ropani")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        hilly.sq_meters_to_hilly(508.74, "ropani", precision=-1)


def test_hilly_to_hilly():
    # Basic conversions
    assert hilly.hilly_to_hilly(1, "ropani", "aana") == pytest.approx(16, rel=1e-2)
    assert hilly.hilly_to_hilly(1, "ropani", "paisa") == pytest.approx(64, rel=1e-2)
    assert hilly.hilly_to_hilly(1, "ropani", "daam") == pytest.approx(256, rel=1e-2)
    assert hilly.hilly_to_hilly(1, "aana", "paisa") == pytest.approx(4, rel=1e-2)
    assert hilly.hilly_to_hilly(1, "aana", "daam") == pytest.approx(16, rel=1e-2)
    assert hilly.hilly_to_hilly(1, "paisa", "daam") == pytest.approx(4, rel=1e-2)
    
    # Reverse conversions
    assert hilly.hilly_to_hilly(16, "aana", "ropani") == pytest.approx(1, rel=1e-2)
    assert hilly.hilly_to_hilly(64, "paisa", "ropani") == pytest.approx(1, rel=1e-2)
    assert hilly.hilly_to_hilly(256, "daam", "ropani") == pytest.approx(1, rel=1e-2)
    
    # Multiple values
    assert hilly.hilly_to_hilly(2.5, "ropani", "aana") == pytest.approx(40, rel=1e-2)
    assert hilly.hilly_to_hilly(3.75, "aana", "paisa") == pytest.approx(15, rel=1e-2)
    assert hilly.hilly_to_hilly(5.5, "paisa", "daam") == pytest.approx(22, rel=1e-2)
    
    # Zero values
    assert hilly.hilly_to_hilly(0, "ropani", "aana") == 0
    assert hilly.hilly_to_hilly(0, "aana", "paisa") == 0
    assert hilly.hilly_to_hilly(0, "paisa", "daam") == 0
    
    # Different precision
    assert hilly.hilly_to_hilly(1, "ropani", "aana", precision=2) == pytest.approx(16.00, rel=1e-2)
    assert hilly.hilly_to_hilly(1, "aana", "paisa", precision=1) == pytest.approx(4.0, rel=1e-1)
    assert hilly.hilly_to_hilly(1, "paisa", "daam", precision=3) == pytest.approx(4.000, rel=1e-3)
    
    # Test case sensitivity
    assert hilly.hilly_to_hilly(1, "ROPANI", "AANA") == pytest.approx(16.00, rel=1e-4)
    assert hilly.hilly_to_hilly(1, "Aana", "Paisa") == pytest.approx(4.00, rel=1e-4)
    assert hilly.hilly_to_hilly(1, "paisa", "DAAM") == pytest.approx(4.00, rel=1e-4) 
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        hilly.hilly_to_hilly(1, "invalid_unit", "ropani")
    with pytest.raises(ValueError):
        hilly.hilly_to_hilly(1, "ropani", "invalid_unit")
    with pytest.raises(ValueError):
        hilly.hilly_to_hilly("1", "ropani", "aana")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        hilly.hilly_to_hilly(-2, "ropani", "aana")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        hilly.hilly_to_hilly(1, "ropani", "aana", precision=-1)
