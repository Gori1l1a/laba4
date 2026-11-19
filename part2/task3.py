def is_palindrome(value):
    '''
    Вход: value(int or str)-слово или число.
    Выход:bool-True, если value - палиндром, False - в противном случае.
    '''
    s=str(value).lower()
    return s==s [::-1]
    