import rupantaran.land.mixed_units as mixed_units


def test_parse_hilly_mixed_unit():
    result = mixed_units.parse_hilly_mixed_unit("2 ropani 3 aana 2 paisa")
    assert isinstance(result, float)


def test_parse_terai_mixed_unit():
    result = mixed_units.parse_terai_mixed_unit("1 bigha 5 kattha 10 dhur")
    assert isinstance(result, float)


def test_terai_mixed_to_hilly_mixed():
    result = mixed_units.terai_mixed_to_hilly_mixed("1 bigha 5 kattha 10 dhur")
    assert isinstance(result, str)


def test_hilly_mixed_to_terai_mixed():
    result = mixed_units.hilly_mixed_to_terai_mixed("2 ropani 3 aana 2 paisa")
    assert isinstance(result, str)
