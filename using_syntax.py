# indentation, functions, blocks, conditionals and loops

# All code blocks are indicated by indentation

# we may choose to annotate the data types - NOT YET COMMON in Python
def addNumbers(x, y): # colon indicates the start of a code block
    '''Tripple quotes are often used for documentation. 
    This is a docstring (use new lines within docstring)
    we may choose to validate the arguments x and y as int'''
    if type(x)== int: # double-equals CHECKS equality (single equals SETS equality)
        return x+y
    elif type(x)==float : # elif means else if
        x = int(x) # take the integer part of x
        return x+y
    else: # else is optional
        pass # very handy as a stand-in jut while you think waht to do
        # continue # does the same within a loop
        return 'problem: x must be an int'
# when the code is no longer indented the code block is ended

'''we could use tripple quotes for multi-line comment
Ive never seen anyone do that!!!'''
# We tend to sue tripple quotes for documentation since it can be retrieved later
print(addNumbers.__doc__) # this is a built-in property of Python
print( addNumbers(3,4) ) # 7
print( addNumbers(3.5,4) ) # 7
# loops
# range(start, stop-before, step)
# for i in range(5): # range will generate values fron m up to n. Here 0, 1, 2, 3, 4
for i in range(2, 5):
    print(addNumbers(i,i), end=', ') # we can override the default new line of print

# using collections tuple list
my_l = [] # an empty list
# for i in range(-1.0, 1.0, 0.1):
for i in range(-10, 11):
    my_l.append(i)
print(my_l)
# shortcut syntax... we can iterate AND populate
my_l = [i for i in range(-10, 11)] # populates the list with every value from the range
my_l.pop() # removes the last value
my_l.pop(2) # removes member at position 2
print(my_l)
    
# tuple   
my_t = tuple(my_l) # we can make a tuple from a list
print(my_t)
# we can use loops to iterate over any ordinal collection
# for value in my_l:
for _ in my_l:
    print(_) # we commonly use _ as a label for an iterable item

