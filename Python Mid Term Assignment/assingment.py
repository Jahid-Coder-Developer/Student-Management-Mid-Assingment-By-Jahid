# Task 01
class Student_Database:
    __student_list = (
        []
    )

    @classmethod
    def add_student(classes, student):
        classes.__student_list.append(student)

    @classmethod
    def get_all_students(classes):
        return classes.__student_list
    
    @classmethod
    def find_student_by_id(classes, student_id):
        for student in classes.__student_list:
            if student.get_student_id() == student_id:
                return student
        return None
    

# Task 02
class Student:

    def __init__(self, student_id, name, department, is_enrolled = False):

        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    # Task 03
        Student_Database.add_student(self)
    # Task 09 - Data Privacy
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_is_enrolled(self):
        return self.__is_enrolled

    # Task 04
    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError(
                f"Error: Student {self.__student_id} is already enrolled."
            )
        self.__is_enrolled = True
        print(f"Success: Student {self.__name} has been enrolled")

    # Task 05
    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError(
                f"Error: Student with ID {self.__name} is not currently enrolled."
            )
        self.__is_enrolled = False
        print(f"Success: Student {self.__name} has been dropped out")

    # Task 06
    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"Student ID: {self.__student_id}")
        print(f"Name      : {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Status    : {status}")
        print("-"*30)

# Task 07 & 08 - Menu & Error Handeling
def menu():

    Student("2634001", "Nadim", "CSE", False)
    Student("2634002", "Jahid", "PSYCHOLOGY", True)
    Student("2634003", "Jubayer", "EEE", False)
    Student("2634004", "Zawad", "PHYSICS", True)
    Student("2634005", "Rinthi", "Chemistry", False)
    Student("2634006", "Shanjida", "Philosophy", True)


    while True:
        print("""       Student Managment Site Of Tejgaon College     """)
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            students = Student_Database.get_all_students()
            if not students:
                print("No students found in the database.")
            else:
                print("""       All Students Information      """)
                for s in students:
                    s.view_student_info()
        elif choice == "2":
            try:
                s_id = input(
                    "Enter Student ID to enrooll (For Example, 2634001): "
                )
                student = Student_Database.find_student_by_id(s_id)
                if not student:
                    raise ValueError(
                        f"Error: Student ID {s_id} does not exist in the database."
                    )
                student.enroll_student()

            except ValueError as e:
                print(e)

        elif choice == "3":
            try:
                s_id = input(
                    "Enter Student ID to drop (For Example, 2634001): "
                )
                student = Student_Database.find_student_by_id(s_id)

                if not student:
                    raise ValueError(
                        f"Error: Student ID {s_id} does not exist in the database."
                    )
                student.drop_student()

            except ValueError as e:
                print(e)

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print(
                "Inbalid choice! Please enter a valid option between 1 and 4."
            )

if __name__ == "__main__":
    menu()