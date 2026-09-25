def main():

    text = input("Enter a string: ")
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    consonants = 0
    for char in text:
        if char.lower() == 'a':
            a += 1
        elif char.lower() == 'e':
            e += 1
        elif char.lower() == 'i':
            i += 1
        elif char.lower() == 'o':
            o += 1
        elif char.lower() == 'u':
            u += 1
        else:
            consonants += 1

    print(f"Number of 'a' : {a}")
    print(f"Number of 'e' : {e}")
    print(f"Number of 'i' : {i}")
    print(f"Number of 'o' : {o}")
    print(f"Number of 'u' : {u}")
    print(f"Number of consonants: {consonants}")

main()    