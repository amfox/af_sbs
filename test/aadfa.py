# coding=utf-8
__author__ = 'TIF'


def autoattribute(d):
    self = d.pop('self')
    for n, v in d.iteritems():
        setattr(self, n, v)


class Test(object):
    def __init__(self, a, b, c, d):
        autoattribute(locals())

    def geta(self):
        return self.a


if __name__ == "__main__":
    a = Test('a', 'b', 'c', 'd')
    print a.geta()