from camel import convert_to_snake

def test_convert_to_snake():
    assert convert_to_snake("name") == "name"
    assert convert_to_snake("firstName") == "first_name"
    assert convert_to_snake("preferredFirstName") == "preferred_first_name"

test_convert_to_snake()
