# Python includes a file access object to work with files

def writeOutput(t):
    '''write the contents of 't' to a text file'''
    # we need a file access object
    # we could use an absolute path to the file
    try:
        # the default is 't' for text
        fobj = open('my_file.txt', 'a') # 'a' will append. If it does not exist it will be created
        # fobj = open('my_file.txt', 'w') # we can also say w for (over)write
        # fobj = open('my_file.txt', 'x') # 'x' Exclusive access
        print(t, file=fobj)
        # print(t)
        fobj.close() # it is a good idea to tidy up
    # we realy should ue try-except with files!!!!!!
    except FileExistsError as fe:
        print(f'Problem: {fe}')
    except FileNotFoundError as fnf:
        print(f'Problem: {fnf}')

if __name__ == '__main__':
    writeOutput('here is a short piece of text')