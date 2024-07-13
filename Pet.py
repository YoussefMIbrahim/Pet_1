class Pet:


    def __init__(self, id, name, age) -> None:

        self.id = id
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


    def __str__(self) -> str:
        pass



