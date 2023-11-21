# we can import from other packages
# when code is imported it runs as if it is part of THIS module
import useful.a
import useful.b # package.module

# here is a global variable within this module
count = 0

# we can use the imported stuff
if __name__ == '__main__':
    print( useful.a.m() )
    print( useful.b.n() )
    print(count) # this will refer the global variable within this module
    print(useful.a.count) # this is in a namespace useful.a
    print(useful.b.count) # this is the namespace useful.b
    # we can mutate values
    useful.a.count += 1 # it was 2 it is now 3
    print(f'The value of count within module a is {useful.a.count} also {useful.a.showCount()}') # 3