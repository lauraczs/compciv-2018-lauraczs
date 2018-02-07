#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]



def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_list` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezlist.py
    """
    return type(ez_list)



##################
# Exercises foo_a through foo_e cover basic list access
##################

def foo_a():
    """
    Return the very first member of `ez_list`
    """
    return ez_list[0]


def foo_b():
    """
    Return the sum of the 2nd and 4th members of
      `ezlist`
    """
    a = ez_list[1]
    b = ez_list[3]
    return a+b



def foo_c():
    """
    Return the very last member of `ez_list`.

    Use a negative index to specify this member
    """
    return ez_list[-1]


def foo_cx():
    """
    Return the type of the object that is the
        second-to-last member of `ez_list`
    """
    x = ez_list[-2]
    return type(x)


def foo_d():
    """
    Return the very last member of the sequence that itself
        is the second-to-last member of `ez_list`
    """
    return ez_list[-2][-1]


def foo_e():
    """
    Calculate and return the length of `ez_list`,  i.e., the
      number of members it contains.
    """
    return len(ez_list)


def foo_f():
    """
    Return the 6th member of `ez_list` as a single,
      semi-colon delimited string

      i.e. the separate values are joined with the
        semi-colon character
    """
    x = ';'
    string = ez_list[5]
    return(x.join(string))
       


def foo_g():
    """
    Return a list that contains the 2nd through 5th
      elements of `ez_list`

      (it should have 4 members total)
    """
    newList = []
    for i in range(1, 5):
        newList.append(ez_list[i])
    return newList



def foo_h():
    """
    Return a list that consists of the last
      3 members of `ez_list` in *reverse* order
    """
    newList = []
    for i in range(1, 4):
        newList.append(ez_list[-i])
    return newList