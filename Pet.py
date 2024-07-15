import itertools

class Pet:
    
    id_count = itertools.count()
    
    def __init__(self, name, age) -> None:

        self.id = next(self.id_count)
        self.name = name
        self.age = age

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value







