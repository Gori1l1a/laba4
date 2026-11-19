from task4 import are_anagrams
import pytest

@pytest.mark.parametrize("a,b,expected", [
    ("кот", "ток", True),
    ("listen", "silent", True,),
    ("", "", True),
    ("А", "а", True),
    ("лес", "село", False)
])

def test_are_anagrams(a,b,expected):
    assert are_anagrams(a,b)==expected