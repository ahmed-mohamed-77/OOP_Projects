import json
from typing import Optional, List, Dict, Any


# User class to store basic user information
class User:
    def __init__(self, username: str, email: str) -> None:
        self.username: str = username
        self.email: str = email


# Customer class inheriting from User, with additional functionality for managing products
class Customer(User):
    def __init__(self, username, email) -> None:
        super().__init__(username, email)  # Initialize the User part of Customer
        self.products = []  # Initialize an empty list to store products

    # Method to add products to the customer's cart
    def add_product(self, cart_item: List[Dict[str, int | Any]]):
        user_found = None
        # Check if the user already exists in the products list
        for idx, product in enumerate(self.products):
            if product["User Name"] == self.username and product["Email"] == self.email:
                user_found = idx  # If found, store the index
                break
        if user_found is not None:
            # If user is found, extend the existing cart with new items
            self.products[user_found]["Cart"][0].update(cart_item[0])
        else:
            # If user is not found, create a new entry for the user
            self.products.append(
                {"User Name": self.username, "Email": self.email, "Cart": cart_item}
            )

    # Method to remove products from the customer's cart
    def remove_product(self, cart_item: List[Dict[str, int | Any]]):
        user_found = None
        # Check if the user already exists in the products list
        for idx, product in enumerate(self.products):
            if product["User Name"] == self.username and product["Email"] == self.email:
                user_found = idx  # If found, store the index
                break

        if user_found is not None:
            cart = self.products[user_found].get(
                "Cart", None
            )  # Get the cart for the user
            if cart is not None:
                try:
                    # Remove items from the cart that are in the cart_item list
                    for item in cart_item[0].keys():
                        cart[0].pop(item, None)
                    
                    print(f"items removed: {cart_item}")
                    self.products[user_found]["Cart"] = cart  # Update the cart
                except ValueError:
                    # Handle the case where the items are not found in the cart
                    print(f"items not found in your cart: {cart_item}")
            else:
                print("cart is empty or not exists")
        else:
            print("user not found")

    # Method to view the cart in JSON format
    def view_cart(self):
        return json.dumps(self.products, indent=4)

    # Method to save the cart to a file
    def save_cart(self, filename, extension: Optional[str] = ".txt"):
        try:
            with open(filename + extension, "w") as file:
                user_found = None
                # Check if the user already exists in the products list
                for idx, product in enumerate(self.products):
                    if (
                        product["User Name"] == self.username
                        and product["Email"] == self.email
                    ):
                        user_found = idx  # If found, store the index
                        break

                if user_found is not None:
                    cart = self.products[user_found].get(
                        "Cart", None
                    )  # Get the cart for the user
                    # Write each item in the cart to the file
                    if cart:
                        for idx, (item, value) in enumerate(cart[0].items(), start=1):
                            file.write(f"{idx} - {item} : {value}\n")

                        print(f"{filename + extension} has been created successfully")
                    else:
                        print("cart is empty or not exists")
                else:
                    print("user not found")
                    return None

        except IOError as e:
            # Handle any I/O errors that occur during file writing
            print(f"An error occurred while writing to the file: {e}")


# Example usage of the Customer class
if __name__ == "__main__":
    customer = Customer("ahmed", "ahmed@gmail.com")
    cart = [
        {
            "Apple iPhone 14": 1400,
            "Nike Air Max 270": 250,
            "Dyson V11 Vacuum Cleaner": 150,
            "Levi's 501 Original Fit Jeans": 300,
            "Sony WH-1000XM4 Headphones": 750,
        }
    ]
    cart2 = [{"Samsung Galaxy S22": 1500, "Bose QuietComfort 45": 250}]
    customer.add_product(cart)  # Add first set of products to the cart
    customer.add_product(cart2)  # Add second set of products to the cart
    customer.remove_product(cart2)  # Remove the second set of products from the cart
    print(customer.view_cart())  # Print the current state of the cart
    customer.save_cart("my_cart")  # Save the cart to a file

    customer_two = Customer("asmaa", "asmaa@gmail.com")
    cart3 = [{"Google Pixel 6": 700, "Adidas Ultraboost": 200}]
    customer_two.add_product(cart3)
    customer_two.add_product(cart)
    print(customer_two.view_cart())
    customer_two.save_cart("asmaa_cart")
