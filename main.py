# import our other modules
import utility
import functions

# by convention we call the main module 'main'
# and conventionally we call the main function 'main'
def main():
    n = functions.askUser()
    # n = 4
    result = utility.checkIfOdd(n)
    print(f'{n} is odd: {result}')


main()