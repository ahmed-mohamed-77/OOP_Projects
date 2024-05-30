import pytest
from oo_projects.source.loyality_system import Loyalty_points  # Replace 'your_module' with the actual module name


def test_points_initial_value():
    loyalty_points = Loyalty_points()
    assert loyalty_points.points == 0

def test_points_negative_initialization():
    with pytest.raises(ValueError, match="Loyalty points starts from 0"):
        Loyalty_points(-10)
        
def test_initial_points():
    loyalty_points = Loyalty_points()
    assert loyalty_points.points == 0

def test_initial_points_with_value():
    loyalty_points = Loyalty_points(10)
    assert loyalty_points.points == 10

def test_initial_points_negative_value():
    with pytest.raises(ValueError, match="Loyalty points starts from 0"):
        Loyalty_points(-10)

def test_earn_point(monkeypatch):
    inputs = iter([
        "item1", "10",
        "item2", "20",
        "q"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    loyalty_points = Loyalty_points()

    points = loyalty_points.earn_point()
    
    assert points == 2
    assert loyalty_points.points == 2

def test_redeem_points_coupon(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "coupon")
    loyalty_points = Loyalty_points(100)
    
    coupon_code, coupon_discount, msg = loyalty_points.redeem_points(50)
    
    assert isinstance(coupon_code, str)
    assert len(coupon_code) == 7
    assert 0.05 <= coupon_discount <= 0.20
    assert "coupon code" in msg.lower()
    assert "coupon discount" in msg.lower()

def test_redeem_points_discount(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "purchase discount")
    loyalty_points = Loyalty_points(100)
    
    discount, msg = loyalty_points.redeem_points(50)
    
    assert 0.05 <= discount <= 0.20
    assert "you get discount on your next purchase" in msg.lower()

def test_redeem_points_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "invalid_choice")
    loyalty_points = Loyalty_points(100)
    
    with pytest.raises(ValueError, match="You Have To Choose From Coupon Or Purchase Discount"):
        loyalty_points.redeem_points(50)
        
if __name__ == "__main__":
    pytest.main()
