customer = {
    "name": "John Doe",
    "age": 30
    }

print(customer["name"])  # Output: John Doe

# get method returns None if the key is not found
print(customer.get("address"))  # Output: None
print(customer.get("age"))  # Output: 30

customer["utsav"] = {"age": 23}

print(customer["utsav"])