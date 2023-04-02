from bank import value

def test_value():
    assert value("hello Jack") == "$0"
    assert value("hi Jack") == "$20"
    assert value("Jack") == "$100"