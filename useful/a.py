# we can say this module in inside the 'useful' namespace
# because it is in the pckage called 'useful'
count = 2

def showCount():
    global count # acces the 'count' in this module
    return count

def m():
    return 'this is function m inside package useful'