def main():

    words = ["eat","tea", "tan", "ate", "nat", "bat"]

    groups = []

    for word in words:
        found = False

        for group in groups:
            if sorted(word) == sorted(group[0]):
                group.append(word)
                found = True
                break

        if not found:
            groups.append([word])

    print(groups)
main()    