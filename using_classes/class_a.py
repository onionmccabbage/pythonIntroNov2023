# in Python EVERYTHING is an object

# the module name is unrelated to the class name
# the problem with normal Python data structures is they have no validation
person = ['Ethel', 32, 'admin']
person[1] = -99 # there is no built in validation for this structure

# a class lets us gather related data and validate the values
# class Person: # by convention we use PascalCase
# class Person(): # by default every class inherits implicitly from 'object'
class Person(object): # we may choose to explicitly inherit from someting else
    '''we often write a docstring to document our class
    Here we declare any methods and properties of the class
    This is available as __doc__ (a built-in)'''
    # built-in parts of python are often called 'dunder' double-underscore before and after
    
    def __init__(self, name, age, level): # every function within a class MUST take 'self'
        '''The initialiser is a bit like a constructor'''
        self.name  = name
        self.age   = age # this will call the setter for 'age'
        self.level = level
    @property # this is called a property decorator. We write a getter and setter method
    def age(self):
        # A mangled name is almost impossible to access from outside this class
        # CAREFUL we CANNOT call it self.age (this would call the function again)
        return self.__age # NB this is called 'name mangling'
    @age.setter
    def age(self, new_age):
        # we can validate the age to be a number
        # if type(new_age)==int or type(new_age)== float and new_age >= 0:
        # Python uses shortcut evaluation: if the first condition fails it will NOT bother checking the second
        if type(new_age) in (int, float) and new_age >= 0:
            self.__age = new_age
        else:
            self.__age = 52 # a sensible default
    @property
    def level(self): # this is the 'getter' method for 'level'
        return self.__level # we always use double-leading-underscore to mangle a name
    @level.setter
    def level(self, new_level):
        # we can validate that the level is permitted
        if new_level in ('user', 'admin', 'guest'):
            self.__level = new_level
        else:
            # raise TypeError('Level must be user admin or guest')
            self.__level = 'guest'
    # write the getter and setter to validate the name as a non-empty string (choose a sensible default)
    # Notice: these functions appear as properties
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        # this is where we enforce the data type of a class property
        # if type(new_name) == 'str' and new_name != '':
        if type(new_name) == str and len(new_name)>0: # str is a type
            self.__name = new_name
        else:
            self.__name = 'Default Name'
    # we can override the built-in __str__ (used by 'print')
    def __str__(self):
        return f'{self.name} is {self.age} with access level {self.level}'

if __name__ == '__main__':
    p1 = Person('Agnes', 34, 'user') # we now have an instance of our 'Person' class
    p2 = Person('Orla', 42, 'admin') 
    # can we mutate the name?
    p1.name = 999 # this should be validated and end up with default name
    print(p1.name, p1.age, p2.level) # we can see properties of our class instance objects
    # print(p1['age'], p2['level']) # or we can use square-bracket notation
    # we can mutate properties of our class
    p1.age = -32 # we need to enforce validation for age
    # remember we cannot directly access p1.__age
    print(f'{p1.name} is {p1.age} and has access level: {p1.level}')
    # what types of data do we have
    print(type(p1.name)) # str - yes it worked!!
    print(Person.__doc__)
    print(p2) # this uses the default print of the class