def main():

    text = input("Enter a string: ")
    sub = input("Enter the substring to search for: ")
    count = 0 # when ever we find a match we will increment this variable

    for i in range(len(text) -  len(sub) + 1):

        if text[i:i + len(sub)] == sub:
            count +=1

    print("The substring appears", count, "times in the string.")        


main()    