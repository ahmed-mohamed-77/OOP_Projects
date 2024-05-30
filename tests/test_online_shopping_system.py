import pytest
import json
from typing import List, Dict
from oo_projects.source.online_shopping_system import Customer  # Adjust the import based on your file structure


@pytest.fixture
def customer():
    return Customer("ahmed", "ahmed@gmail.com")


@pytest.fixture
def customer_two():
    return Customer("asmaa", "asmaa@gmail.com")


@pytest.fixture
def cart():
    return [
        {
            "Apple iPhone 14": 1400,
            "Nike Air Max 270": 250,
            "Dyson V11 Vacuum Cleaner": 150,
            "Levi's 501 Original Fit Jeans": 300,
            "Sony WH-1000XM4 Headphones": 750,
        }
    ]


@pytest.fixture
def cart2():
    return [{"Samsung Galaxy S22": 1500, "Bose QuietComfort 45": 250}]


@pytest.fixture
def cart3():
    return [{"Google Pixel 6": 700, "Adidas Ultraboost": 200}]


def test_add_product(customer, cart, cart2):
    customer.add_product(cart)
    customer.add_product(cart2)
    cart_state = json.loads(customer.view_cart())
    assert len(cart_state) == 1
    assert cart_state[0]["Cart"][0]["Apple iPhone 14"] == 1400
    assert cart_state[0]["Cart"][0]["Samsung Galaxy S22"] == 1500


def test_remove_product(customer, cart, cart2):
    customer.add_product(cart)
    customer.add_product(cart2)
    customer.remove_product(cart2)
    cart_state = json.loads(customer.view_cart())
    assert len(cart_state) == 1
    assert "Samsung Galaxy S22" not in cart_state[0]["Cart"][0]


def test_view_cart(customer, cart, cart2):
    customer.add_product(cart)
    customer.add_product(cart2)
    cart_view = customer.view_cart()
    assert isinstance(cart_view, str)
    cart_state = json.loads(cart_view)
    assert len(cart_state) == 1
    assert cart_state[0]["User Name"] == "ahmed"


@pytest.mark.parametrize(
    "cart_item, expected_count",
    [
        ([{"Apple iPhone 14": 1400}], 1),
        ([{"Samsung Galaxy S22": 1500}], 1),
        ([{"Apple iPhone 14": 1400, "Samsung Galaxy S22": 1500}], 2),
    ],
)
def test_add_product_param(customer, cart_item, expected_count):
    customer.add_product(cart_item)
    cart_state = json.loads(customer.view_cart())
    assert len(cart_state[0]["Cart"][0]) == expected_count


def test_add_product_multiple_carts(customer_two, cart, cart3):
    customer_two.add_product(cart3)
    customer_two.add_product(cart)
    cart_state = json.loads(customer_two.view_cart())
    assert len(cart_state) == 1
    assert "Google Pixel 6" in cart_state[0]["Cart"][0]
    assert "Apple iPhone 14" in cart_state[0]["Cart"][0]
