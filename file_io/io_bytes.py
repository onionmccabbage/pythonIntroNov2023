
def writeBytes():
    '''write bytes to a byte file'''
    b = b'this is a string of bytes' #this will be a byte string
    # we really should ue try-except
    fobj = open('mybytes', 'ab', encoding='UTF8') # 'a' will append 'b' will write as bytes
    fobj.write(b)

def readBytes():
    '''read bytes back in'''
    fobj = open('mybytes', 'rb')
    retrieved = fobj.read()
    return retrieved

if __name__ == '__main__':
    writeBytes()
    b = readBytes()
    print(b)