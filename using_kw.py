# we can also unpack keyword arguments
def decide(**kwargs): # kwargs is a dict of all the keyword arguments
    '''decide what to do based on the keyword aguments'''
    # conditionally respond to the arguments
    return kwargs

# we can use both
def useBoth(*args, **kwargs):
    ''' if there are any arguents they will exist in a tuple and a dict'''
    resultObt = []
    if len(args)>0:
        ''' we have at least one postitional argument'''
        resultObt.append(args)
    resultObt.append(kwargs)
    return resultObt



if __name__  == '__main__':
    # r = decide(n=1)
    r = decide(n=1, m=2, a=[7,6,5], b=(4,3,2))
    print(r) # a dictionary
    s = useBoth(3, 2 ,1 , m=5, n=6, l=[])
    print(s)