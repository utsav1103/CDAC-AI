def main():

    marks = int(input("Enter your marks: "))

    if marks >= 90 and marks <= 100:
        print("Grade: A")
    elif marks >= 80 and marks < 90:
        print("Grade: B")
    elif marks >= 70 and marks < 80:
        print("Grade: C")
    elif marks >= 60 and marks < 70:
        print("Grade: D")
    else:
        print("Grade: F")            
main()    