# we can use the 'with' operator to ensure clean working with file access objects

def writeCleanly(t):
    '''Here we write text to a file and automatically 
    close the file access object'''
    try:
        with open('my_log.txt', 'a') as fobj:
            fobj.write(t) # I could use chunks to write
        # When the 'with' operator ends, the file access object will be automatically closed
    except Exception as err:
        print(f'Oh dear... {err}')

if __name__ == '__main__':
    writeCleanly('this is nicely output and the file access object is automatically closed')
