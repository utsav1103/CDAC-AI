def main():
    student = {}
    name = input("Enter name:")
    marks = int(input("Enter marks:"))
    student['name'] = name
    student['marks'] = marks
    print("Name:",student['name'])
    print("Marks:",student['marks'])
    if student['marks'] <= 35:
        print("Result: Fail")
    else:
        print("Result: Pass")
main()