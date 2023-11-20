# import our other modules
import utility # we do not need to import dependencies
import random # if we use NOTHING it STILL imports the module
# import functions
# alternatively
# from functions import askUser
# or...
from functions import askUser as au

# by convention we call the main module 'main'
# and conventionally we call the main function 'main'
def main():
    # n = functions.askUser()
    # n = askUser()
    n = au()
    # n = 4
    result = utility.checkIfOdd(n)
    print(f'{n} is odd: {result}')

if __name__ == '__main__':
    main() # only call the main function if this module is being run direclty (not via import)