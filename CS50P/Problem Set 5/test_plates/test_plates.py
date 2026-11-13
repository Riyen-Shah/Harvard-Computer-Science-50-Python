from plates import is_valid

def test_first_letters():
    assert is_valid("H1") == False
    assert is_valid("H") == False
    assert is_valid("123") == False
    assert is_valid("Hell0") == False
    assert is_valid("Yoo1") == True

def test_max():
    assert is_valid("Hello") == True
    assert is_valid("Wasssap") == False

def test_numbers():
    assert is_valid("He11o") == False
    assert is_valid("Hell10") == True

def test_punctuation():
    assert is_valid("Hello!") == False
    assert is_valid("Woah.") == False
