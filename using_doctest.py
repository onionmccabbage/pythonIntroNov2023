# we can unit test a module to ensure riguour
import doctest

def cube(x):
    '''return the cube of x
    >>> cube(3)
    27
    >>> cube(-2)
    -8'''
    return x**3


if __name__ == '__main__':
    # c = cube(3)
    # print(c) # 27
    doctest.testmod(verbose=True)