# Python is a scripting language. It is interpreted by the python executable

# identifiers, variables and immediate code

a = 3 # an int
b = 7 # a floating point value
print(a/b, type(a/b))
# maths: + - / * // ** and %
print(3**2) # ** is to the power of
print(b//a) # how many times does it go into...
print(b%a) # modulo arythmetic
# we have += and -= also *= /= but NOT ++ or --

# Python has an immutable string type
s = 'is it coffee yet?'
print(type(s)) # a string is a zero-based ordinal collection of characters
# we can slice members of the string
s = 'it is nearly time for coffee'
print( s[3] ) # i
print( s[0:8:2] ) # start:stop-before:step
# s[0] = 'I' # nope
print( s[::-1] ) # useful to show backwards

# tuple - an immutable ordinal collection of any data type
t = (7,6,5,4,'hello', True, a, b, s ) # careful True and False
print(t, type(t))
print(t[3:7])
# t[4] = 'nope' # this will fail

# using quotes in python: single, double, tripple or double-tripple quotes
s1 = 'we \'can\' use "single" quotes'
s2 = "we can \"also\" use 'double' quotes"
s3 = '''If we need we can \tuse \ttripple \tquotes
this will preserver whitespace 
such as new lines,           tabs, etc.'''
s4 = """same applies to \ntripple \ndouble \nquotes 
like this"""
print(s1, s2, s3, s4) # by default 'print' will always end with a new line character

# the list type: a mutable ordinal collection of any data type
l = [7,6,5,4, 'coffee!!', b, a, t]
l[1] = -6 # we can mutate members of a list
print(l ,type(l))

