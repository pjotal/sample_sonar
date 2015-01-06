
class Person(object):

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone
