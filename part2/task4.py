def are_anagrams(a,b):
    '''
    Вход:a(str),b(str)
    Выход:bool-True, если a и b - анаграммы, False - в противном случае.
    '''
    return sorted(a.lower())==sorted(b.lower())