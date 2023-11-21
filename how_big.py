import sys

def main():
    '''how big can Python go?'''
    print(10**100000) # the limit is system resources

if __name__ == '__main__':
    main()
    print(sys.maxsize) # the largest single object Python can manage in memory
    print(sys.float_info)