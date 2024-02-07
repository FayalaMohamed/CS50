from bank import value

def test_value():
    assert value("twitter") == 100
    assert value("0123") == 100
    assert value("tWitter") == 100
    assert value("tWItter")==100
    assert value("tWitter!*")==100
    assert value("hi") == 20
    assert value("hello")==0
    assert value("Hello !")==0