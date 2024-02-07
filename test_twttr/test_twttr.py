from twttr import shorten

def test_shorten():
    assert shorten("twitter")=="twttr"
    assert shorten("0123")=="0123"
    assert shorten("tWitter")=="tWttr"
    assert shorten("tWItter")=="tWttr"
    assert shorten("tWitter!*")=="tWttr!*"