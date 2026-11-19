def combine_dict(d1,d2):
    '''
    Вход:d1(dict),d2(dict).
    Выход:dict-новый словарь, состоящий из d1 и d2.
    '''
    result=d1.copy()
    result.update(d2)
    return result