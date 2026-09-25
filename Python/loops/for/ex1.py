# for item in "Python":
#     print(item)


# for item in ["Python", "Java", "C++"]:
# for item in [1,2,3,4,5,6,7,8,9,10 ]:
    # print(item)


# for item in range(10):
#     print(item)

# for item in range(50 ,100, 3 ):
    # print(item)

def main():

    prices = [10, 20, 30, 40, 50]
    total = 0
    for price in prices:
        total += price
        print(f"Total so far: {total}")

main()