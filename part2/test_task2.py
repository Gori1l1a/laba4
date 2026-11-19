from task2 import find_unique
import pytest

@pytest.mark.parametrize('items,expected',[
    ([], []),
    (['a'], ['a']),
    (['a','b'], ['a','b']),
    ([1,2,3,2,1], [3]),
    ([4,4,4,4],[])
])

def test_find_unique(items,expected):
    assert find_unique(items)==expected