def main():

    name = input("Enter your name :")
    if name.isnumeric():
        print("Name can not be number")    

    elif len(name) < 4:
        print("Name must be at least 4 characters long")


    elif len(name) > 20:
        print("Name can not exceed 20 characters")

    else:
        print("Name Looks good!")    


main()