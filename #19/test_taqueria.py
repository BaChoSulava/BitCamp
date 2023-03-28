from taqueria import users_order

def test_users_order():
    assert users_order("Taco") == "Total: $6.00"
    assert users_order("Baja Taco") == "Total: $12.00"