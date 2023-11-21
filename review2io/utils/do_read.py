def readLog():
    '''read from the log'''
    fin = open('review_log.txt', 'r')
    r = fin.read()
    return r