first = 'Gitthal'
last = 'Chan'

full_name = f"{first}-{last}"

print (full_name)


print("Hey! cutie " * 7)

#* inbuilt len function

name = "gitthal chan"
print(name)

print(f"Your name has {len(name)} characters.")

#! inbuilt . functions

print(name.upper())
print(name.lower())
print(name.title())    

print(name.find("chan"))    
#finds the index of the first occurrence of the substring
print(name.replace("chan", "Cutie Chan")) 

'gitthal' in name
print('gitthal' in name)  # returns True if 'gitthal' is found in name, else False
print('Gitthal' in name)  # returns False because of case sensitivity