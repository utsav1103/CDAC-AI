products = []
next_id = 1

def welcome():
    print("*"*90)
    print("Welcome to the Product management system :")
    print("*"*90)
    print("Select the option from below to perform the operation :")
    print("*"*90)
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Products")
    print("6. Exit")


    print("*"*90)
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def add_product():
    global next_id
    while True:
        
        name = input("Enter product name: ")
        if name.strip() == "":
            print("Product name cannot be empty.")
            continue
        break
       
    while True:

        category = input("Enter product category: ")
        if category.strip() == "":
            print("Product category cannot be empty.")
            continue
        break
       
    while True:
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print("Product price cannot be zero or negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")
    while True:
        try:
            quantity = int(input("Enter product quantity: "))
            if quantity < 0:
                print("Product quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the quantity.")

    product = {
            "id": next_id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }
    products.append(product)
    next_id += 1

#print(products)

def view_product():
    if not products:
        print("No products available.")
    else:
        print("*"*90)
        print("products list: ")
        print("*"*90)
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']},Quantity: {product['quantity']}")
        print("*"*90)
    
#view_products()

def search_product():
    search_choice = input("Search by (1) Name or (2) Id? Enter 1 or 2 :")
    if search_choice == "1":
        try:
            name = input ("Enter product name to search: ")

            for product in products:
                if product['name'] == name:
                    return product
            print("Product not found.")
        except ValueError:
            print("Invalid input...")
    elif search_choice == "2":
        try:
            product_id = int(input("Enter product id to search: "))
            found = False


            for product in products:
                if product['id'] == product_id:
                    found = True
                    return product
            if not found:
                print("Product not found.")
        except ValueError:
            print("Invalid input....")


def update_product():
    product_id = int(input("Enter product id to update:" ))
    for product in products:
        if product['id'] == product_id:
            while True:

                name = input("Enter updated product name: ")

                if name.strip() == "":
                    print("Product name cannot be empty.")
                    continue
                product['name'] = name
                break
            while True:
                category = input("Enter updated product category: ")
                if category.strip() == "":
                    print("Product category cannot be empty.")
                    continue
                product['category'] = category
                break

            while True:
                try:
                    price = float(input("Enter updated product price: "))
                    if price <= 0:
                        print("Product price must be greater than zero.")
                        continue
                    product['price'] = price
                    break
                except ValueError:
                    print("Invalid input")
            while True:
                try:
                    quantity = int(input("Enter updated product quantity: "))

                    if quantity < 0:
                        print("Quantity must be more than zero and not negative")
                        continue
                    product['quantity'] = quantity
                    break
                except ValueError:
                    print("invalid input...")
            print("Product updated successfully.")
            return
    print("Product not found.")


def delete_product():
    while True:
        try:
            product_id = int(input("Enter product id to delete: "))
            for product in products:
                if product['id'] == product_id:
                    products.remove(product)
                    print("Product removed successfully. ")
                    return                
    
            print("Product not found.")
            return
        except ValueError:
            print("Invalid input...")



while True:
    choice = welcome()
    if choice == 1:
        add_product()
    elif choice == 2:
        view_product()
    elif choice == 3:
        update_product()
    elif choice == 4:
        delete_product()
    elif choice == 5:
        search_product()
    elif choice == 6:
        break
    elif choice is None:
        continue
    else:
        print("Invalid choice. Please try again.")
