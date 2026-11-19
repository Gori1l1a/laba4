def count_words(text):
    '''
    Вход: str   - текст.
    Выход: int- кол-во слов в тексте.
    '''
    if not text:
        return 0
    return len(text.split())