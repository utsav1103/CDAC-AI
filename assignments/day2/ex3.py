def main():

    email = input("Enter your Email: ")
    if email.count('@') == 1:
        domain  = email.split('@')[1]
        print(domain)

    else:
        print("Invalid email")    

main()    