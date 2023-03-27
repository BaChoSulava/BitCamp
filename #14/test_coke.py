from coke import calculations

def calculations_test():
    assert calculations(25) == "Amount Due: 25"
    assert calculations(10) == "Amount Due: 40"
    assert calculations(5) == "Amount Due: 45"
    assert calculations(30) == "Amount Due: 50"
    assert calculations(50) == "Change Owed: 0"
    assert calculations(60) == "Change Owed: 10"



