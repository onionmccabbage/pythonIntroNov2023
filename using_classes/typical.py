# here is  as top-level class

class Typical():
    '''Properties are id and userId
    Both must be positive integers'''
    def __init__(self, id, userId):
        self.id = id
        self.userId = userId
    # write get/set methods for the properties
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, new_id):
        if type(new_id)==int and new_id > 0:
            self.__id
        else:
            raise TypeError('id must be a positive integer')
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, new_userId):
        if type(new_userId)==int and new_userId > 0:
            self.__userId
        else:
            raise TypeError('userId must be a positive integer')   
    