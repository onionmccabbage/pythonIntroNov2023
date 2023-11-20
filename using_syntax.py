# indentation, functions, blocks, conditionals and loops

# All code blocks are indicated by indentation

# we may choose to annotate the data types - NOT YET COMMON in Python
def addNumbers(x, y): # colon indicates the start of a code block
    '''Tripple quotes are often used for documentation. 
    This is a docstring (use new lines within docstring)
    we may choose to validate the arguments x and y as int'''
    if type(x)== int: # double-equals CHECKS equality (single equals SETS equality)
        return x+y
    else: # else is optional
        return 'problem: x must be an int'
# when the code is no longer indented the code block is ended

'''we could use tripple quotes for multi-line comment
Ive never seen anyone do that!!!'''
# We tend to sue tripple quotes for documentation since it can be retrieved later
print(addNumbers.__doc__) # this is a built-in property of Python


