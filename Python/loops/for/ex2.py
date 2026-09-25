def main():

    numbers = [5, 2, 5, 2, 2]

    for x in numbers:
        # print('x' * x)
        output = ''
        for count in range(x):
            output += 'x'
        print(output)

main()    