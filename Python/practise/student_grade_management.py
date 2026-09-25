# students grade management system
import json
students = []

next_id = 1

def calculate_grade(marks):

    if marks >= 85:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    #print("Grade:", grade)
    return grade


def enroll_student():
    global next_id
    while True:
        name = input("Enter student name: ").strip()
        if name == "" or not name.replace(" ", "").isalpha():
            print("Name cannot be empty ")
            continue
    
        else:
            print("Name:", name)
            break

    while True:
        course = input("Enter course: ").strip()

        if course == "" or not course.replace(" ","").isalpha():
            print("Course can not be empty")
            continue
        else:
            print("Course:", course)
            break

    while True:
        try:
            marks = float(input("Enter marks:"))
            if 0 <= marks <= 100:
                break
            
            else:
                print("Marks must be between 0-100..")
        except ValueError:
            print("Please enter valid number...")

    grade = calculate_grade(marks)
    print("Grade:", grade)

    student = {
        "id": next_id,
        "name": name,
        "course": course,
        "marks": marks,
        "grade": grade
    }
    students.append(student)
    next_id += 1


#print(students)

def display_students():
    if not students:
        print("NO Students are there: ")
        print ("*"*60)
    else:
        print("Students List: ")
        print("*"*60)
        for student in students:
            print(f"{'ID':<5}{'Name':<20}{'Course':<15}{'Marks':<10}{'Grade':<8}")
            print("-"*60)
            print(f"{student['id']:<5}{student['name']:<20}{student['course']:<15}{student['marks']:<10}{student['grade']:<8}")



def search_student():
    search_choice = input("Search by (1) Name or by (2) ID or by (3) Course - ")
    if search_choice == "1":
        try:
            name = input("Enter student name to search : ")
            matches = []
            for student in students:
                if name.lower() in student['name'].lower():
                    matches.append(student)

            if matches:
                for student in matches:
                    print(student)
            else:
                print("Student not found")
        except ValueError:
            print("invalid input")

    elif search_choice == "2":
        try:
            student_id = int(input("Enter id to search student"))

            found = False
            for student in students:
                if student['id'] == student_id:
                    found = True
                    break
            if not found:
                print("student not found")
        except ValueError:
            print("Invalid input")

    elif search_choice == "3":
            
        course = input("Enter course name to search : ")
        matches = []
        for student in students:
            if course.lower() in student['course'].lower():
                matches.append(student)

        if matches:
            for student in matches:
                print(student)
        else:
            print("Student not found")

    else:
        print("invalid search choice")
    
        print("Student not found")

def update_student():
    try:
        student_id = int(input("Enter student id to update : "))
        for student in students:
            if student['id'] == student_id:
                print("Student found : ", student)

                name = input("Enter new name : ").strip()

                if name != "":
                    if name.replace(" ", "").isalpha():
                        student['name'] = name
                    else:
                        print("invalid name. keep the old name>")

                course = input("Enter new course : ").strip()

                if course != "":
                    student['course'] = course


                marks_input = input("Enter new marks : ").strip()

                if marks_input != "":
                    try:
                        marks = float(marks_input)

                        if 0 <= marks <= 100:
                            student['marks'] = marks

                            student['grade'] = calculate_grade(marks)

                        else:
                            print("Marks must be between 0 t9 100")

                    except ValueError:
                        print("Invalid marks")

                print("Student updated successfully...")
                print(student)
                return
            print("Student not found.")
    except ValueError:
        print("Invalid student ID: ")


def delete_student():
    while True:
        try :
            student_id = int(input("Enter id to delete the student : "))
            for student in students:
                if student['id'] == student_id:
                    students.remove(student)
                    print("student removed successfully")
            print("student not found")
        except:
            print("Invalid input")


def save_to_json():
    with open("student.json","w") as file:
        json.dump(students,file,indent=4)

    print("Students saved successfully.")


def load_from_json():
    global students

    try:
        with open("student.json","r") as file:
            students = json.load(file)

        print("students loaded successfully.")

    except FileNotFoundError:
        print("student.json not found")

    except json.JSONDecodeError:
        print("Invalid json file..")

def main():
    while True:
        print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
        print("1. Enroll Student")
        print("2. Cohort Directory")
        print("3. Query Records")
        print("4. Revise Evaluation")
        print("5. Purge Record")
        print("6. Save to JSON")
        print("7. Load from JSON")
        print("8. Terminate")

        choice = input("Enter your choice: ")

        if choice == "1":
            enroll_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            save_to_json()

        elif choice == "7":
            load_from_json()

        elif choice == "8":
            print("Program terminated.")
            break

        else:
            print("Invalid choice.")


main()