def askUser():
    '''ask the user for an integer'''
    # the following code is in a block scope
    # specifically this code is within the function scope
    while True:
        i=input('Please enter an integer value')
        try:
            i_int = int(float(i)) # this is conventional
            return i_int
        except ValueError as v:
            pass # handle the exception silently

# this is in the global scope
a=1

if __name__ == '__main__':
    '''We always use this to exercise the current module (check this module works as intended)'''
    #this code is within a conditional block scope
    i = askUser()
    print(f'User entered {i}')