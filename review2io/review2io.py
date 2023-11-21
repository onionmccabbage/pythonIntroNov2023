from utils.do_write import writeLog
from utils.do_read import readLog
from utils.do_ask import askUser
from utils. do_validate import checkValid

def main():
    # loop
    while True:
        # ask for input from the user
        try:
            i = askUser()
            # validate it is a non-empty string
            i = checkValid(i)
        except Exception as e:
            print(e)
        # check for 'quit'
        if i == 'quit':
            break
        # check for 'read'
        if i=='read':
            log = readLog()
            print(log)
        else:
            writeLog(i)

if __name__ == '__main__':
    main()