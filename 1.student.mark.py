# Practical Work 1 - Student Mark Management

students = []
courses = []
marks = {}

def input_number_of_students():
    try:
        n = int(input("Number of students: "))
        return n
    except:
        print("Invalid number!")
        return 0

def input_student_information():
    sid = input("Student ID: ").strip()
    name = input("Student Name: ").strip()
    dob = input("Student DoB (dd/mm/yyyy): ").strip()

    students.append((sid, name, dob))
    print("Student added.")

def input_number_of_courses():
    try:
        n = int(input("Number of courses: "))
        return n
    except:
        print("Invalid number!")
        return 0

def input_course_information():
    cid = input("Course ID: ").strip()
    name = input("Course Name: ").strip()

    courses.append((cid, name))
    print("Course added.")

def select_course_and_input_marks():
    print("\nAvailable courses:")
    for i, (cid, name) in enumerate(courses):
        print(f"{i+1}. {cid} - {name}")

    try:
        choice = int(input("Select course (number): "))
        choice -= 1
        if choice < 0 or choice >= len(courses):
            print("Invalid course selection!")
            return
    except:
        print("Invalid input!")
        return

    course_id = courses[choice][0]

    print(f"\nInput marks for course: {courses[choice][1]}")
    for sid, name, dob in students:
        try:
            m = float(input(f"Mark for {name} ({sid}): "))
            marks[(course_id, sid)] = m
        except:
            print("Invalid mark, skipped.")

def list_students():
    print("\n=== STUDENTS ===")
    for sid, name, dob in students:
        print(f"{sid} - {name} - {dob}")
    print()


def list_courses():
    print("\n=== COURSES ===")
    for cid, name in courses:
        print(f"{cid} - {name}")
    print()


def show_student_marks_for_course():
    print("\nAvailable courses:")
    for i, (cid, name) in enumerate(courses):
        print(f"{i+1}. {cid} - {name}")

    try:
        choice = int(input("Select course (number): "))
        choice -= 1
        if choice < 0 or choice >= len(courses):
            print("Invalid course selection!")
            return
    except:
        print("Invalid input!")
        return

    course_id = courses[choice][0]
    course_name = courses[choice][1]

    print(f"\n=== Marks for course: {course_name} ===")
    for sid, name, dob in students:
        key = (course_id, sid)
        if key in marks:
            print(f"{sid} - {name} : {marks[key]}")
        else:
            print(f"{sid} - {name} : No mark")
    print()

def main():
    while True:
        print("""
====== STUDENT MARK MANAGEMENT ======
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
            n = input_number_of_students()
            for _ in range(n):
                input_student_information()

        elif choice == "2":
            n = input_number_of_courses()
            for _ in range(n):
                input_course_information()

        elif choice == "3":
            select_course_and_input_marks()

        elif choice == "4":
            list_students()

        elif choice == "5":
            list_courses()

        elif choice == "6":
            show_student_marks_for_course()

        elif choice == "0":
            print("Bye")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
