# we can say this module in inside the 'useful' namespace
# because it is in the pckage called 'useful'
count = 2

def showCount():
    global count # acces the 'count' in this module
    return count

def m():
    return 'this is function m inside package useful'

# call imported
def main():
    print(more.here()) # found!!

if __name__ == '__main__':
    import subpack.more as more# use a path when this module is run directly
    main()
else:
    import useful.subpack.more as more # use a relative path when this is already imported 