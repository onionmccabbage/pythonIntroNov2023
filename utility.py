from math import sqrt
def checkIfOdd(n):
    '''return True if odd, False if not odd'''
    if n%2 !=0: # the value is not an even number
        return True
    else:
        return False
    
def showSqrt(n):
    return sqrt(n)

# any immediate code will be run on import

# When Python runs a module directly it will ALWAYS set __name__ to '__main__'
# this is useful, so we can check if the module is being run directly
if __name__ == '__main__': # we know this module is being run directly
    # print(f'this is the module called {__name__}') # __main__ whn run directly
    # check the functions operate as intended
    for _ in range(0,10):
        print(f'{_} is odd: {checkIfOdd(_)}')
        print(f'{_} square root: {showSqrt(_)}')

# else:
#     print(f'This module has been imported as {__name__}')
