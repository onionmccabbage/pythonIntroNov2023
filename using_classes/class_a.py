# the module name is unrelated to the class name
# the problem with normal Python data structures is they have no validation
person = ['Ethel', 32, 'admin']
person[1] = -99 # there is no built in validation for this structure

# a clas lets us gather related data and validate the values
class Person: # by convention we use PascalCase
    def __init__(self, name, age, level): # every function within a class MUST take 'self'
        '''The initialiser is a bit like a constructor'''
        self.name  = name
        self.age   = age
        self.level = level

if __name__ == '__main__':
    p1 = Person('Agnes', 34, 'user') # we now have an instance of our 'Person' class
    p2 = Person('Orla', 42, 'admin') 
    print(p1, p2)