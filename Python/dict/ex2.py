contact = input("Enter contact number : ")

#mapping
digit_map = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""

for ch in contact: 
    # output += digit_map[ch] + " "  # This will throw an error if ch is not in digit_map
    output += digit_map.get(ch, "!") + " " 

print(output)