def main():

    name = input("Enter your name:")

    words = name.split()

    if len(words) == 1:
        print(words[0])
    else:
        result = ""

        for word in words[:-1]:
            result += word[0].upper() + "."

        result += words[-1]

        print(result)            

main()    