from task3 import is_palindrome
import pytest

@pytest.mark.parametrize('value,expected',[
    ('radar',True),
    ('1234',False),
    ("привет",False),
    ("",True),
    ("123321",True),
])

def test_is_palindrome(value,expected):
    assert is_palindrome(value)==expected