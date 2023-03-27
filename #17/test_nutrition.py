from nutrition import check_for_calories

def test_check_for_calories():
    assert check_for_calories("Apple") == 130
    assert check_for_calories("Avocado") == 50
    assert check_for_calories("Sweet Cherries") == 100