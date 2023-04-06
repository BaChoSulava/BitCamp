from seasons import age_in_minutes

def test_age_in_minutes():
    assert age_in_minutes("1987, 1, 3") == "nineteen million, sixty-eight thousand, four hundred and eighty minutes"