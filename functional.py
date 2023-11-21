def raisePower(n=2, m=3): # we may provide defaults 
    '''raise m to the power of n'''
    return m**n

# single asterisk * will unpack a list or tuple
def doStuff(*args): # all the positional arguents will be collected into a tuple
    '''if there are no args, just return False
    If there is one arg, return that
    If there are two args, multiply them
    If there are three args, do something'''
    if len(args)==0:
        return False
    elif len(args)==1:
        return args[0] # the margument at position zero
    elif len(args)==2:
        return args[0]*args[1]
    elif len(args)==3:
        return args[0]+args[1]+args[2]
    # print(args)

if __name__ == '__main__':
    # r=doStuff(2,3,99)
    # r=doStuff(2,3)
    # r=doStuff(2)
    r=doStuff()
    print(r)
    # these are called keyword arguments
    # r = raisePower(n=3,m=2)
    # we can still provide just values
    # these are postional arguments
    # s = raisePower(4,3) # this will be n then m
    # we can combine positional and keyword arguments
    # positional must come first
    # t = raisePower(-2, m=4)
    # print(r,s,t)
