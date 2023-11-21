# There are useful ordinal collections such as tuple, list, string
# Also we have a non-ordinal collection called a dictionary
d = {'fname':'Timnit', 'sname':'Gebru', 'age':32, 'admin':True}
t = ('Google', 'Microsoft', 'Python') # a tuple can contain a dict, set, list, string etc.
d['Employers'] = t
# we can iterate over the members
for k, v in d.items(): # careful these are in no particular order
    print(f'{k} contains {v}')

# also there is a set - a colection of unique members
s2 = {10, 11, 12}
# we can use an asterisk to unpack a collection into its members
s = {6,5,4,4,8,6,3,t,None,'words', *s2} # cannot add a dict or list or set
s.add(9)
s.remove(6)
l =[s, d, t]
print(s)
print(l)

# a list may contain ANY data type
my_list = [s, l, t, d]
print('\n',my_list)

