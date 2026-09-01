def main():

    text = input("Enter a string: ")
    comp = ""
    count = 1

    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i+1]:
            count += 1

        else:
            comp += text[i] + str(count)
            count = 1    
    if len(comp) < len(text):
        print(comp)

    else:
        print(text)    
main()    