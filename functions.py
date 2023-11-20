def askUser():
    '''ask the user for an integer'''
    while True:
        i=input('Please enter an integer value')
        try:
            i_int = int(float(i)) # this is conventional
            return i_int
        except ValueError as v:
            pass # handle the exception silently

