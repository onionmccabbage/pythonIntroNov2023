
def writeParts(n):
    '''we will write 'n' to a text file using buffer'''
    try:
        fobj = open('log2.txt', 'a') # 'a' will append
        size = len(n) # we now know how many characters we need to output
        offset = 0
        chunk  = 24 # we choose a buffer of 24 characters
        while True:
            if offset>size: # there is nothing left to output
                fobj.close() # so we close out file access object
                break
            else:
                fobj.write( n[offset:offset+chunk] ) # slice from offset to chunk
                offset += chunk
    except Exception as e:
        print(f'Problem: {e}')

if __name__ == '__main__':
    writeParts('Here is a very long amount of pointless badly speeeled text which I will commit to a file in a short while honstly I will')