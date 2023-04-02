import pytest
from fuel import calc_percentage

def test_calc_percentage():
    assert calc_percentage("3/4") == 75
    assert calc_percentage("1/4") == 25
    assert calc_percentage("4/4") == "F"
    assert calc_percentage("0/4") == "E"
    
    # 
    # assert calc_percentage("1.5/3") == "F"
    # assert calc_percentage("5/4") == "E"
    

def test_errors():
    with pytest.raises(ZeroDivisionError):
        calc_percentage("4/0")
    with pytest.raises(ValueError):
        calc_percentage("three/four")
        calc_percentage("1.5/3")

