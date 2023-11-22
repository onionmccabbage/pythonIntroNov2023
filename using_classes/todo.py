# here is a class that inherits from a top level class
from typical import Typical

class Todo(Typical):
    '''Extend the parent class and 
    add properties for title and completed'''
    def __init__(self, id, userId, title, completed):
        # first we call the __init__ of the parent class
        super().__init__(id, userId)
        # then we can add other properties
        self.title = title
        self.completed = completed
    # get/set methods for properties of this class
    @property 
    def title (self):
        return self.__title
    @title.setter
    def title(self, new_title):
        if type(new_title)== str and len(new_title)>0:
            self.__title
        else:
            raise TypeError('title must be a non empty string')
    @property
    def completed(self):
        return self.__completed
    @completed.setter
    def completed(self, new_completed):
        if type(new_completed) == bool:
            self.__completed = new_completed
        else:
            raise TypeError('Completed must be a boolean')


if __name__ == '__main__':
    todo_a = Todo(2, 9, 'Have Lunch', False)
    print(todo_a.id)