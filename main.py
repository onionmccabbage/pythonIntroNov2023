# import our other modules
import utility
import functions

def main():
    n = functions.askUser()
    # n = 4
    result = utility.checkIfOdd(n)
    print(f'{n} is odd: {result}')


main()