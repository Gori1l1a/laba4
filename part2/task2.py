def find_unique(items):
    '''
    Вход:items(list)-список элементов.
    Выход:list-список уникальных элементов.
    '''
    if not items:
        return []
    
    unique=[]
    for i in items:
        if items.count(i)==1:
            unique.append(i)
    
    return unique