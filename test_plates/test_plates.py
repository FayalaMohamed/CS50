from plates import is_valid


def test_is_valid():
    assert is_valid("twittr") == True
    assert is_valid("twittddr") == False
    assert is_valid("") == False
    assert is_valid("01d") == False
    assert is_valid("tWIttr") == True
    assert is_valid("tWi!*") == False
    assert is_valid("hi") == True
    assert is_valid("hello") == True
    assert is_valid(" !lo") == False
    assert is_valid("Heo !") == False
    assert is_valid("hel12") == True
    assert is_valid("h112") == False
    assert is_valid("hel1p") == False
    assert is_valid("hel10") == True
    assert is_valid("hel01") == False
