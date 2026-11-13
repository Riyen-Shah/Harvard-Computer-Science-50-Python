from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

def test_h():
    assert value("Hey") == 20
    assert value("hi") == 20

def test_other():
    assert value("Welcome") == 100
    assert value("Whats up?") == 100

def test_int():
    assert value("1 moment please") == 100
    assert value ("Please wait 1 minute") == 100
