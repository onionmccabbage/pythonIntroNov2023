# we can format strings in many ways

# old-skool
a = 'Python'
b = 'formatting'
f = 3.14745498465 # an approximation of 'pi'

s = 'the language {0} can apply {1} in many ways. E.g. {2:0.4f}'.format(a, b, f)
#                                               we can specify the accuracy like this
s2 = f'Alternatively we just use {b} within {a} like this {f:0.2f}'
print(s, s2)