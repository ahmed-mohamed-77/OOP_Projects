from typing import Union, Any

a = "Ahmed Mohamed"
b = ["Ahmed", "Channel"]


class Order:
    def __init__(self, cart: list, customer: str) -> None:
        self.cart = cart
        self._customer = customer
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, name):
        if self._customer != name:
            raise ValueError("cannot change user name")

    def add_item(self, item: list | str):
        self.cart.append(item)

    def __len__(self) -> int:
        return len(self.cart)

    def __call__(self):
        print(f"{self.customer}")

    def __str__(self) -> str:
        return f"username: {self.customer}\ncart: {" - ".join(self.cart)}".title()

    def __bool__(self):
        return len(self.cart) > 0
    
    def __add__(self, other: Union[list , str]) -> "Order":
        new_cart = self.cart.copy()
        
        if isinstance(other, str):
            new_cart.append(other)
        elif isinstance(other, list): 
            new_cart.extend(other)
        
        return Order(new_cart, self.customer)
    
    def __getitem__(self, key: int) -> Any:
        return self.cart[key]
    
    def __setitem__(self, key: Any, value: Any) -> None:
        self.cart[key] = value




order = Order(["Laptop", "Mouse", "KeyBoard"], "ahmed mohamed")

order += ["Usb Stick", "SSD"]
order += "RTX 4080 Super"
order = order + ["RTX 4090", "Fans"]
print(order.cart)
order[3] = "HDD"
print(order.cart)
