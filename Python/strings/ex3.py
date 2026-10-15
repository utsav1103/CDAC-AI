def main():
    text = input("Enter a string:")
    print(text[::-1])
    count = 0
    for i in text.lower():
        if i in {'a','e','i','o','u'}:
            count += 1
    print(f"Number of vowel characters: {count}")

main()    