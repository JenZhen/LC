#!/usr/bin/python


def add1(x):
    x += 1
    print "inside function: ", x
    return x

def test():
    x = 1
    add1(x)
    print x

if __name__ == "__main__":
    print 'hi'
    test()
