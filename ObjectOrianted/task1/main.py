#Tạo một lớp Student gồm có student_id, full_name, gpa. Viết chương trình:
#1.Thêm sinh viên
#2.In ra danh sách sinh viên
#3.Tìm kiếm sinh viên theo mã
#4.In ra top 3 sinh viên có gpa cao nhất
from ObjectOrianted.task1.Student_Management import Students
from ObjectOrianted.task1.Student import Student

if __name__ == '__main__':
    student_list = Students()

    while True:
        print('============================================')
        print('1.Add new student')
        print('2.Print all students')
        print('3.Find a student by id')
        print('4.Print top 3 students having highest gpa')
        print('5.Exit')
        print('============================================')

        try:
            choice = int(input('Enter your choice: '))
            if choice not in (1, 2, 3, 4, 5):
                print('Invalid choice')
            if choice == 5:
                break
        except ValueError:
            print('Invalid input')
            continue

        if choice == 1:
            try:
                student_id = int(input('Enter student ID: '))
                name = input('Enter student name: ')
                gpa = float(input('Enter student GPA: '))
                student = Student(student_id, name, gpa)
                student_list.add_student(student)
                print(f'Student {student.get_id()} added.')
            except ValueError:
                print('Invalid input')
        elif choice == 2:
            students = student_list.get_all_students()
            for student in students:
                print(student.to_string())
            if not students:
                print('No students added yet')
        elif choice == 3:
            try:
                student_id = int(input('Enter student ID: '))
                student = student_list.find_student(student_id)
                if not student:
                    print('Student not found')
                else:
                    print(student.to_string())
            except ValueError:
                print('Invalid input')
        elif choice == 4:
            top_3_students = student_list.get_top_3_students()
            if not top_3_students:
                print('No students having highest gpa')
            else:
                for student in top_3_students:
                    print(student.to_string())