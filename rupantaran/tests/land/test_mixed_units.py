import pytest
import rupantaran.land.mixed_units as mixed_units



def test_parse_terai_mixed_unit():
    # Basic conversions
    assert mixed_units.parse_terai_mixed_unit("1 bigha 5 kattha 10 dhur") == pytest.approx(8632.08, rel=1e-2)
    assert mixed_units.parse_terai_mixed_unit("2 bigha 10 dhur") == pytest.approx(13714.56, rel=1e-2)
    
    # Different unit combinations
    assert mixed_units.parse_terai_mixed_unit("2 bigha") == pytest.approx(13545.26, rel=1e-2)
    assert mixed_units.parse_terai_mixed_unit("3 kattha") == pytest.approx(1015.89, rel=1e-2)
    assert mixed_units.parse_terai_mixed_unit("4 dhur") == pytest.approx(67.72, rel=1e-2)
    
    # Zero values
    assert mixed_units.parse_terai_mixed_unit("0 bigha 0 kattha") == pytest.approx(0, rel=1e-2)
    
    # Test case sensitivity
    assert mixed_units.parse_terai_mixed_unit("1 BIGHA 5 KATTHA") == pytest.approx(8463.29, rel=1e-2)
    assert mixed_units.parse_terai_mixed_unit("2 Bigha 10 Dhur") == pytest.approx(13714.56, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        mixed_units.parse_terai_mixed_unit("invalid string")
    with pytest.raises(ValueError):
        mixed_units.parse_terai_mixed_unit("1 invalid_unit")
    with pytest.raises(ValueError):
        mixed_units.parse_terai_mixed_unit("bigha 1")
    
    # Test negative values
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        mixed_units.parse_terai_mixed_unit("-1 bigha 5 kattha")
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        mixed_units.parse_terai_mixed_unit("1 bigha -5 kattha")

def test_parse_hilly_mixed_unit():
    # Basic conversions
    assert mixed_units.parse_hilly_mixed_unit("2 ropani 3 aana 2 paisa") == pytest.approx(1128.7, rel=1e-1)
    assert mixed_units.parse_hilly_mixed_unit("1 ropani 0 aana 5 paisa") == pytest.approx(548.47, rel=1e-2)
    
    # Different unit combinations
    assert mixed_units.parse_hilly_mixed_unit("2 ropani") == pytest.approx(1017.44, rel=1e-2)
    assert mixed_units.parse_hilly_mixed_unit("3 aana") == pytest.approx(95.37, rel=1e-2)
    assert mixed_units.parse_hilly_mixed_unit("4 paisa") == pytest.approx(31.8, rel=1e-2)
    assert mixed_units.parse_hilly_mixed_unit("5 daam") == pytest.approx(9.95, rel=1e-2)
    
    # Zero values
    assert mixed_units.parse_hilly_mixed_unit("0 ropani 0 aana") == pytest.approx(0, rel=1e-2)
    
    # Test case sensitivity
    assert mixed_units.parse_hilly_mixed_unit("2 ROPANI 3 AANA") == pytest.approx(1128.8, rel=1e-1)
    assert mixed_units.parse_hilly_mixed_unit("1 Ropani 5 Paisa") == pytest.approx(548.47, rel=1e-2)
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        mixed_units.parse_hilly_mixed_unit("invalid string")
    with pytest.raises(ValueError):
        mixed_units.parse_hilly_mixed_unit("1 invalid_unit")
    with pytest.raises(ValueError):
        mixed_units.parse_hilly_mixed_unit("ropani 1")
    
    # Test negative values
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        mixed_units.parse_hilly_mixed_unit("-2 ropani 3 aana")
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        mixed_units.parse_hilly_mixed_unit("2 ropani -3 aana")



def test_sq_meters_to_terai_mixed():
    # Basic conversions
    assert mixed_units.sq_meters_to_terai_mixed(8632.08,precision=2) == "1 bigha 5 kattha 9.82 dhur"
    assert mixed_units.sq_meters_to_terai_mixed(13714.56) == "2 bigha 0 kattha 10.0000 dhur"
    
    # Zero values
    assert mixed_units.sq_meters_to_terai_mixed(0) == "0 bigha 0 kattha 0.0000 dhur"
    
    # Different precision
    assert mixed_units.sq_meters_to_terai_mixed(8632.08, precision=2) == "1 bigha 5 kattha 9.82 dhur"
    assert mixed_units.sq_meters_to_terai_mixed(13714.56, precision=1) == "2 bigha 0 kattha 10.0 dhur"
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        mixed_units.sq_meters_to_terai_mixed("invalid")
    
    # Test negative values
    with pytest.raises(ValueError, match="Input area must be non-negative"):
        mixed_units.sq_meters_to_terai_mixed(-8632.08)
    
    # Test negative precision
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        mixed_units.sq_meters_to_terai_mixed(8632.08, precision=-1)


def test_sq_meters_to_hilly_mixed():
    # Basic conversions
    assert mixed_units.sq_meters_to_hilly_mixed(1082.55) == "2 ropani 2 aana 0 paisa 0.7487 daam"
    assert mixed_units.sq_meters_to_hilly_mixed(522.5) == "1 ropani 0 aana 1 paisa 2.9196 daam"
    
    # Zero values
    assert mixed_units.sq_meters_to_hilly_mixed(0) == "0 ropani 0 aana 0 paisa 0.0000 daam"
    
    # Different precision
    assert mixed_units.sq_meters_to_hilly_mixed(1082.55, precision=2) == "2 ropani 2 aana 0 paisa 0.75 daam"
    assert mixed_units.sq_meters_to_hilly_mixed(522.5, precision=1) == "1 ropani 0 aana 1 paisa 2.9 daam"
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        mixed_units.sq_meters_to_hilly_mixed("invalid")
    
    # Test negative values
    with pytest.raises(ValueError, match="Input area must be non-negative"):
        mixed_units.sq_meters_to_hilly_mixed(-1082.55)
    
    # Test negative precision
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        mixed_units.sq_meters_to_hilly_mixed(1082.55, precision=-1)


def test_terai_mixed_to_hilly_mixed():
    # Basic conversions
    assert mixed_units.terai_mixed_to_hilly_mixed("1 bigha 5 kattha 10 dhur") == "16 ropani 15 aana 2 paisa 1.2513 daam"
    assert mixed_units.terai_mixed_to_hilly_mixed("2 bigha 10 dhur") == "26 ropani 15 aana 1 paisa 1.2663 daam"
    
    # Zero values
    assert mixed_units.terai_mixed_to_hilly_mixed("0 bigha 0 kattha 0 dhur") == "0 ropani 0 aana 0 paisa 0.0000 daam"
    
    # Different precision
    assert mixed_units.terai_mixed_to_hilly_mixed("1 bigha 5 kattha 10 dhur", precision=2) == "16 ropani 15 aana 2 paisa 1.25 daam"
    
    # Test case sensitivity
    assert mixed_units.terai_mixed_to_hilly_mixed("1 BIGHA 5 KATTHA") == "16 ropani 10 aana 1 paisa 0.0452 daam"
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        mixed_units.terai_mixed_to_hilly_mixed("invalid string")
    with pytest.raises(ValueError):
        mixed_units.terai_mixed_to_hilly_mixed("1 invalid_unit")
    
    # Test negative values
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        mixed_units.terai_mixed_to_hilly_mixed("-1 bigha 5 kattha")
    
    # Test negative precision
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        mixed_units.terai_mixed_to_hilly_mixed("1 bigha 5 kattha", precision=-1)


def test_hilly_mixed_to_terai_mixed():
    # Basic conversions
    assert mixed_units.hilly_mixed_to_terai_mixed("2 ropani 3 aana 2 paisa") == "0 bigha 3 kattha 6.6663 dhur"
    assert mixed_units.hilly_mixed_to_terai_mixed("16 ropani 15 aana 2 paisa 1.2313 daam",precision=2) == "1 bigha 5 kattha 10.00 dhur"
    
    # Zero values
    assert mixed_units.hilly_mixed_to_terai_mixed("0 ropani 0 aana 0 paisa") == "0 bigha 0 kattha 0.0000 dhur"
    
    # Different precision
    assert mixed_units.hilly_mixed_to_terai_mixed("2 ropani 3 aana 2 paisa", precision=2) == "0 bigha 3 kattha 6.67 dhur"
    
    # Test case sensitivity
    assert mixed_units.hilly_mixed_to_terai_mixed("2 ROPANI 3 AANA 2 PaiSa" ) == "0 bigha 3 kattha 6.6663 dhur"
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        mixed_units.hilly_mixed_to_terai_mixed("invalid string")
    with pytest.raises(ValueError):
        mixed_units.hilly_mixed_to_terai_mixed("1 invalid_unit")
    
    # Test negative values
    with pytest.raises(ValueError, match="Input value must be non-negative"):
        mixed_units.hilly_mixed_to_terai_mixed("-2 ropani 3 aana")
    
    # Test negative precision
    with pytest.raises(ValueError, match="Precision must be non-negative"):
        mixed_units.hilly_mixed_to_terai_mixed("2 ropani 3 aana", precision=-1)
