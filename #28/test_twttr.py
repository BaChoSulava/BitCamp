from twttr import ommit_vowels

def test_ommit_vowels():
    assert ommit_vowels("Twitter") == "Twttr"
    assert ommit_vowels("What's your name?") == "Wht's yr nm?"
    assert ommit_vowels("CS50") == "CS50"

 