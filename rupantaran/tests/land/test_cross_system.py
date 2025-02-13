import pytest
import rupantaran.land.cross_system as cross_system


def test_terai_to_hilly():
    # Basic conversions
    assert cross_system.terai_to_hilly(1, "bigha", "ropani") == pytest.approx(13.31, rel=1e-2)
    assert cross_system.terai_to_hilly(1, "kattha", "aana") == pytest.approx(10.65, rel=1e-2)
    assert cross_system.terai_to_hilly(1, "dhur", "paisa") == pytest.approx(2.12, rel=1e-2)
    
    # Multiple values
    assert cross_system.terai_to_hilly(3.75, "kattha", "aana") == pytest.approx(39.94, rel=1e-2)
    
    # Zero values
    assert cross_system.terai_to_hilly(0, "bigha", "ropani") == 0
    assert cross_system.terai_to_hilly(0, "kattha", "aana") == 0
    assert cross_system.terai_to_hilly(0, "dhur", "paisa") == 0
    
    # Different precision
    assert cross_system.terai_to_hilly(1, "bigha", "ropani", precision=2) == pytest.approx(13.31, rel=1e-2)
    assert cross_system.terai_to_hilly(1, "kattha", "aana", precision=1) == pytest.approx(10.6, rel=1e-1)
    
    # Test case sensitivity
    assert cross_system.terai_to_hilly(1, "BIGHA", "ROPANI") == pytest.approx(13.31, rel=1e-2)
    assert cross_system.terai_to_hilly(1, "Kattha", "Aana") == pytest.approx(10.65, rel=1e-2)
    assert cross_system.terai_to_hilly(1, "dHuR", "PaIsA") == pytest.approx(2.12, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        cross_system.terai_to_hilly(1, "invalid_unit", "ropani")
    with pytest.raises(ValueError):
        cross_system.terai_to_hilly(1, "bigha", "invalid_unit")
    with pytest.raises(ValueError):
        cross_system.terai_to_hilly("1", "bigha", "ropani")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        cross_system.terai_to_hilly(-2, "bigha", "ropani")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        cross_system.terai_to_hilly(1, "bigha", "ropani", precision=-1)


def test_hilly_to_terai():
    # Basic conversions
    assert cross_system.hilly_to_terai(1, "ropani", "bigha") == pytest.approx(0.075, rel=1e-2)
    assert cross_system.hilly_to_terai(1, "aana", "kattha") == pytest.approx(0.094, rel=1e-2)
    assert cross_system.hilly_to_terai(1, "paisa", "dhur") == pytest.approx(0.47, rel=1e-2)
    
    # Multiple values
    assert cross_system.hilly_to_terai(2.5, "ropani", "bigha") == pytest.approx(0.1875, rel=1e-2)
    assert cross_system.hilly_to_terai(3.75, "aana", "kattha") == pytest.approx(0.3525, rel=1e-2)
    assert cross_system.hilly_to_terai(5.5, "paisa", "dhur") == pytest.approx(2.585, rel=1e-2)
    
    # Zero values
    assert cross_system.hilly_to_terai(0, "ropani", "bigha") == 0
    assert cross_system.hilly_to_terai(0, "aana", "kattha") == 0
    assert cross_system.hilly_to_terai(0, "paisa", "dhur") == 0
    
    # Different precision
    assert cross_system.hilly_to_terai(1, "ropani", "bigha", precision=2) == pytest.approx(0.08, rel=1e-2)
    assert cross_system.hilly_to_terai(1, "aana", "kattha", precision=1) == pytest.approx(0.1, rel=1e-1)
    
    # Test case sensitivity
    assert cross_system.hilly_to_terai(1, "ROPANI", "BIGHA") == pytest.approx(0.075, rel=1e-2)
    assert cross_system.hilly_to_terai(1, "Aana", "Kattha") == pytest.approx(0.094, rel=1e-2)
    assert cross_system.hilly_to_terai(1, "PaIsA", "dHuR") == pytest.approx(0.47, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        cross_system.hilly_to_terai(1, "invalid_unit", "bigha")
    with pytest.raises(ValueError):
        cross_system.hilly_to_terai(1, "ropani", "invalid_unit")
    with pytest.raises(ValueError):
        cross_system.hilly_to_terai("1", "ropani", "bigha")

    # Test negative value raises error
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        cross_system.hilly_to_terai(-2, "ropani", "bigha")
    
    # Test negative precision raises error
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        cross_system.hilly_to_terai(1, "ropani", "bigha", precision=-1)
