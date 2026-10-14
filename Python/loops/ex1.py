def main():

    for i in range(2,21,2):
        print(i)
    print("*"*20)
    for i in range(1,10):
        if i == 4:
            continue
        if i == 8:
            break
        print(i)

main()