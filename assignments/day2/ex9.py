def main():

    text = input("Enter a string: ")
    longest = ""

    for i in range(len(text)):
        for j in range(i + 1 , len(text) + 1):
            sub = text[i:j]

            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub

    print("The longest palindrome in the string is:", longest)    

main()    