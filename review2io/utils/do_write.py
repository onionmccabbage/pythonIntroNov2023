def writeLog(t):
    # write to a text file (append)
    fout = open('review_log.txt', 'a')
    # fout.write(t)
    fout.write(f'{t}\n')