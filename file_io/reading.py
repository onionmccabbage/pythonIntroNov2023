# we can use a file access object to read back from a file

def readText():
    '''read from a text file'''
    try:
        fobj = open('my_file.txt', 'r') # 'r' will read from a text file
        # result = fobj.read() # read the whole file
        # result = fobj.readline() # read a line
        result = fobj.readlines() # read all the line as a list of strings
        return result
    except Exception as e:
        print(f'Problem: {e}')

if __name__ == '__main__':
    r = readText()
    print(r)