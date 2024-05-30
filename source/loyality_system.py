import json
import string
import random


class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_if = str(customer_id)
        self.name: str = name


class Loyalty_points:
    def __init__(self, points: int = 0) -> None:
        if points < 0:
            raise ValueError("Loyalty points starts from 0")
        self.points = int(points)

    # its one time trade
    def earn_point(self):
        print("Welcome to our store")
        print("To wrap your order press [q - quit]")

        purchase_dict = {}
        total_amount = 0

        while True:
            customer_purchase = (
                input("what would you like to buy: ".title()).strip().lower()
            )

            if customer_purchase in ["q", "quit"]:
                break

            purchase_value = int(input("Enter the Amount: ").strip())
            purchase_dict[customer_purchase] = purchase_value

        for value in purchase_dict.values():
            total_amount += value

        total_points = round(0.05 * total_amount)
        purchase_dict["Total Amount"] = f"{total_amount} $"
        purchase_dict["Points Received"] = f"{total_points} pts"

        print(json.dumps(purchase_dict, indent=4))

        if self.points > 0:
            self.points += total_points
        else:
            self.points = total_points
        return total_points

    def redeem_points(self, amount):
        redeem = ["coupon", "purchase discount"]
        print("which way you want to redeem you points")
        choice = str(
            input("choose between Coupon or purchase discount: ".title())
            .strip()
            .lower()
        )
        if choice not in redeem:
            raise ValueError(
                "You Have to Choose from Coupon or purchase discount".title()
            )
        else:

            if self.points >= amount:
                if choice == "coupon":
                    coupon_code = "".join(
                        random.choices(string.ascii_letters + string.digits, k=7)
                    )
                    coupon_discount = round(random.uniform(0.05, 0.20), 2)
                    self.points -= amount
                    return (
                        coupon_code,
                        coupon_discount,
                        f"coupon code: {coupon_code}\ncoupon discount: {coupon_discount}%".title(),
                    )
                elif choice == "purchase discount":
                    self.points -= amount
                    discount = round(random.uniform(0.05, 0.20), 2)
                    return (
                        discount,
                        f"you get discount on your next purchase {discount}%",
                    )
            else:
                print("Not enough points to redeem")


class VIPCustomer(Customer, Loyalty_points):
    def __init__(self, customer_id: str, name: str, points: int = 0) -> None:
        Customer.__init__(self, customer_id, name)
        Loyalty_points.__init__(self, points)


class Transaction:
    """to store relevant information about each transaction"""

    def __init__(self, transaction_id: str, customer: str, amount: str) -> None:
        self.transaction_id = str(transaction_id)
        self.customer: str = customer
        self.amount: int = amount


class Transaction_history:
    def __init__(self) -> None:
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction):
        self.transactions.remove(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            yield transaction.transaction_id, transaction.customer, transaction.amount


vip = VIPCustomer(519879, "ahmed")

transactions = [
    Transaction(59733, "ahmed", "+58777"),
    Transaction(57955, "mohamed", "-11987"),
    Transaction(85421, "mmm", "+187"),
]

history = Transaction_history()
for transaction in transactions:
    history.add_transaction(transaction)

for idx, transaction in enumerate(history.show_transactions(), start=1):
    print(idx, transaction)
