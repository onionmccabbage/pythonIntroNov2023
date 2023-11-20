# we write code within modules (files with .py)
# we can ask the user for input
# we will look at exception handling
# also while

# we can define our own exception types
class MyCustomException(Exception): # this custom class is a type of exception
    pass

def askUser():
    '''Ask user to enter an int'''
    # EVERY user input is ALWAYS a string
    v = input('Enter a number: ')
    # v = int(v) # try to convert the string to an int
    # v = float(v) # try to convert the string to a float
    # after lunch we will handle exceptions!!!
    try:
        v = int(float(v)) # try to convert the string to an int (via a float)
    except ValueError as ve: # this will be run if a ValueError occurs
        print('Value Error')
    except Exception as e: # handle all other exceptions
        print('some unknown problem has occured')
    # finally:
    #     print('the finally block will always run')
    # raise(MyCustomException) # here our exception will happen
    if type(v)==int or type(v)==float:
        return v
    else:
        # pass # we could choose to do nothing
        # raise TypeError('We need a number') # it is common practice to raise an exception
        return 0 # we can choose to return just a sensble default value

# we will KEEP asking until they enter a positive number
g = -99
while g<1:
    g = askUser()

print(g)