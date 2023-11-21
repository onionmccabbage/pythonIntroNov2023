# everything that is not in a block of code is in the global scope
count = 1 # this is in the global scope

def fn(): # this is a block scope
    global count # we now have access to the global variable
    count = 9
    return count

if __name__ == '__main__':
    print(count) # 1
    print(fn()) # 9
    print(count) # 9