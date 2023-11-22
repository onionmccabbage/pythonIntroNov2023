# we will explore range, generator and comprehension
for i in range(0, 100): # more efficient (just a range object in memory)
    print(i)

# here is a tuple
for i in (0,1,2,3,4,5,6,7,8,9): # all the values need to exist in memory
    print(i)

r = range(0,1000) # range will yield the next value as we need it (instead of persisting in memory)
print(type(r))

# we can use a range to make a generator
g = (i*i for i in range(0,100000000000000000))
# or 
g = (i*i for i in r) # we can use a generator to provide calculated values without needing a fnction
print(type(g)) # a generator
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9
print(next(g)) # 16
print(next(g)) # 25

# comprehension - comprehensively deal with every member of a collection
odds_l = [ i for i in range(1, 11111111, 2) ] # these values now all exist in memory
odds_g = ( i for i in range(1, 11111111, 2) ) # these values DO NOT exist in memory
odds   = list( i for i in range(1, 11111111, 2) ) # these values DO exist in memory
print(type(odds_l))
print(odds)