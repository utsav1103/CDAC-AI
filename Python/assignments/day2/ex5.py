def main():

    text = input("Enter a string: ")

    words = text.split(" ")
    res = ""

    for word in words:
        res = res + word[0].upper() + word[1:].lower() + " "
        
    print(res)

main()    