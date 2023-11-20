# we write code within modules (files with .py)
# we can ask the user for input

def askUser():
    '''Ask user to enter an int'''
    # EVERY user input is ALWAYS a string
    v = input('Enter a number: ')
    # v = int(v) # try to convert the string to an int
    # v = float(v) # try to convert the string to a float
    # after lunch we will handle exceptions!!!
    v = int(float(v)) # try to convert the string to an int (via a float)
    if type(v)==int or type(v)==float:
        return v
    else:
        raise TypeError('We need a number') # it is common practice to raise an exception

askUser()