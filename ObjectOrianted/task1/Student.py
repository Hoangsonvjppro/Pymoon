class Student():
    def __init__(self, student_id, name, gpa):
        self.__id = student_id
        self.name = name
        self.gpa = gpa

    def get_id(self):
        return self.__id

    def get_gpa(self):
        return self.gpa

    def to_string(self):
        return f'{self.__id} {self.name} {self.gpa}'