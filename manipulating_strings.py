# here are some utilites to work with strings of text (remember - strings are immutable)

def find(long, short):
    ''' find a short string within a longer string'''
    i = long.find(short) # find will return the position where the string first appears
    return i

def combine(word_l):
    '''join together a number of strings into one string'''
    result = '-'.join(word_l) # join is a method the string type
    return result

if __name__ == '__main__':
    '''exercise the code'''
    l = 'is it time for our lunch break?'
    s = 'time'
    position = find(l, s)
    print(f'the word {s} first appears at position {position}')
    # Python alows us to initialize several variables all at the same time
    (a,b,c,d,e)='one', 'two', 'three', 'four', 'five'
    print(a,b,c,d,e)
    q = [a,b,c,d,e]
    print( combine(q) ) # one-two-three-four-five

