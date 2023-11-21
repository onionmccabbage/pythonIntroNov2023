# everything that is not in a block of code is in the global scope
count = 1 # this is in the global scope

def fn(): # this is a block scope
    global count # we now have access to the global variable
    count = 9 # this is indented, so it is inside a block. It is in a block scope
    return count

def other():
    count = 3 # a different block scope
    return count

if __name__ == '__main__':
    print(count) # 1
    print(fn()) # 9
    print(other()) # 3
    # print(count) # 1
    print(count) # 9