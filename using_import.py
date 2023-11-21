# we can import from other packages
import useful.a
import useful.b # package.module

# we can use the imported stuff
if __name__ == '__main__':
    useful.a.n()
    useful.b.m()