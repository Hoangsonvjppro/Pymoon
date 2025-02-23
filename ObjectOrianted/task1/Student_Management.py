class Students():
    def __init__(self):
        self.__students = []

    def add_student(self, s):
        self.__students.append(s)

    def get_all_students(self):
        return self.__students

    def find_student(self, student_id):
        for student in self.__students:
            if student.get_id() == student_id:
                return student
        return None

    def get_top_3_students(self):
        if len(self.__students) == 0:
            return []
        return  sorted(self.__students, key=lambda student: student.get_gpa(), reverse=True)[:3]