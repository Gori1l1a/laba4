from task5 import combine_dict
import pytest

@pytest.mark.parametrize("d1,d2,expected",[
    ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}),
    ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 1, "b": 3, "c": 4}),
    ({}, {"a": 1}, {"a": 1}),
    ({"a": 1}, {}, {"a": 1}),
    ({},{},{})
])

def test_combine_dict(d1,d2,expected):
    assert combine_dict(d1,d2)==expected