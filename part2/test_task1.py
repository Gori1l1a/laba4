from task1 import count_words
import pytest

@pytest.mark.parametrize('text, expected', [
    ('Привет, друг, как дела',4),
    ('',0),
    ("Вася переехал в другой город 10 лет назад",8),
    ("  ",0),
    ("Программа выполнены успешно",3)
])

def test_count_words(text,expected):
    assert count_words(text) == expected
    
