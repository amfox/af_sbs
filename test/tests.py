#coding=utf-8
__author__ = 'TIF'


def empty_copy(obj):
    class Empty(obj.__class__):
        def __init__(self):
            pass
    newcopy = Empty()
    newcopy.__class__ = obj.__class__
    return newcopy

class MyClass(object):
    def __init__(self):
        print 'MyClass'

    def __copy__(self):
        newcopy = empty_copy(self)
        return newcopy

if __name__ == "__main__":
    import copy
    y = MyClass()
    print hex(id(y))

    z = copy.copy(y)
    print hex(id(z))