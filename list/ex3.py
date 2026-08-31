#* 2d list

def main():

    matrix = [[1, 2, 3],
              [4, 5, 6],    
              [7, 8, 9]]

    print(matrix[1][0])  # Output: 1
    print(matrix[0][1])  # Output: 2
    print(matrix[0][2])  # Output: 3

    for row in matrix:
        for element in row:
            print(element, end=' ')

main()    