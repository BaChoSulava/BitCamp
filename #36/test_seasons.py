from seasons import age_in_minutes

def test_age_in_minutes():
    assert age_in_minutes("1987, 03, 01") == "eighteen million, nine hundred and eighty-six thousand, four hundred minute"
    assert age_in_minutes("2019, 09, 24") == "one million, eight hundred and fifty-seven thousand, six hundred minute"