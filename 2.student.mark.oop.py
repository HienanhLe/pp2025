# Practical Work 2 - Apply OOP
class Student:
    def __init__(self, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
    def get_id(self):
        return self.__sid
    def get_name(self):
        return self.__name
    def get_dob(self): 
        return self.__dob
    def list(self):
        print(f"{self.__sid} - {self.__name} - {self.__dob}")
    @staticmethod
    def input():
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Student DoB (dd/mm/yyyy): ")
        return Student(sid, name, dob)
class Course:
    def __init__(self, cid, name):
        self.__cid = cid
        self.__name = name
    def get_id(self):
        return self.__cid
    def get_name(self):
        return self.__name
    def list(self):
        print(f"{self.__cid} - {self.__name}")
    @staticmethod
    def input():
        cid = input("Course ID: ")
        name = input("Course Name: ")
        return Course(cid, name)
class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def input_students(self):
        try:
            n = int(input("Number of students: "))
        except:
            print("Invalid number!")
            return
        for _ in range(n):
            s = Student.input()
            self.students.append(s)
            print("Student added.")
    def list_students(self):
        print("\n== STUDENTS ===")
        for s in self.students:
            s.list()
        print()
    def input_courses(self):
        try:
            n = int(input("Number of courses: "))
        except:
            print("Invalid number!")
            return
        for _ in range(n):
            c = Course.input()
            self.courses.append(c)
            print("Course added.")
    def list_courses(self):
        print("\n=== COURSES ===")
        for c in self.courses:
            c.list()
        print()
    def input_marks(self):
        if not self.courses:
            print("No courses available!")
            return
        print("\nAvailable courses:")
        for i, c in enumerate(self.courses):
            print(f"{i+1}. {c.get_id()} - {c.get_name()}")
        try:
            choice = int(input("Select course (number): ")) - 1
            if choice < 0 or choice >= len(self.courses):
                print("Invalid course selection!")
                return
        except:
            print("Invalid input!")
            return
        course = self.courses[choice]
        cid = course.get_id()
        print(f"\nInput marks for course: {course.get_name()}")
        for s in self.students:
            try:
                m = float(input(f"Mark for ({s.get_name()}): "))
                self.marks[(cid, s.get_id())] = m
            except:
                print("Invalid mark, skipped.")
    def show_marks(self):
        if not self.courses:
            print("No courses available!")
            return
        print("\nAvailable courses:")
        for i, c in enumerate(self.courses):
            print(f"{i+1}. {c.get_id()} - {c.get_name()}")
        try:
            choice = int(input("Select course (number): ")) - 1
            if choice < 0 or choice >= len(self.courses):
                print("Invalid course!")
                return
        except:
            print("Invalid input!")
            return
        course = self.courses[choice]
        cid = course.get_id()
        print(f"\n=== Marks for courses: {course.get_name()} ===")
        for s in self.students:
            key = (cid, s.get_id())
            if key in self.marks:
                print(f"{s.get_id()} = {s.get_name()} : {self.marks[key]}")
            else:
                print(f"{s.get_id()} = {s.get_name()} : No mark")
        print()
def main():
    mm = MarkManager()
    while True:
        print("""
====== STUDENT MARK MANAGEMENT (OOP) ======
1. Input number of students + their info
2. Input number of courses + their info
3. Select a course and input marks
4. List students
5. List courses
6. Show student marks for a course
0. Exit
""")
        choice = input("Your choice: ").strip()

        if choice == "1":
            mm.input_students()
        elif choice == "2":
            mm.input_courses()
        elif choice == "3":
            mm.input_marks()
        elif choice == "4":
            mm.list_students()
        elif choice == "5":
            mm.list_courses()
        elif choice == "6":
            mm.show_marks()
        elif choice == "0":
            print("Bye")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
