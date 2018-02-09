from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    def fooage(p):
        return p['age']
    return sorted(PEOPLE_LIST, key=fooage)


def oldest():
    """
    sort by age in descending order
    """
    def fooage(p):
        return p['age']
    return sorted(PEOPLE_LIST, key=fooage, reverse = True)


def name_reverse_alpha():
    def fooname(p):
        return p['name']
    return sorted(PEOPLE_LIST, key=fooname, reverse = True)


def country_then_age():
    def fooboth(p):
        return (p['country'], p['age'])
    return sorted(PEOPLE_LIST, key=fooboth)
