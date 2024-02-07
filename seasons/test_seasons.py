from seasons import sing
import pytest

def test_sing():
    assert sing("2022-02-14")=="Five hundred twenty-five thousand, six hundred minutes"
    assert sing("2021-02-14"
                ) == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit):
        sing("200-13-13")
