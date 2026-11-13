from twttr import shorten

def test_a():
    assert shorten("Sam ran") == "Sm rn"
    assert shorten("Max sat") == "Mx st"
def test_e():
    assert shorten("Ben went") == "Bn wnt"
    assert shorten("Ted met Jeff") == "Td mt Jff"
def test_i():
    assert shorten("Tim sits") == "Tm sts"
    assert shorten("Jim will swim") == "Jm wll swm"
def test_o():
    assert shorten("Tom got hot") == "Tm gt ht"
    assert shorten("Bob jogs") == "Bb jgs"
def test_u():
    assert shorten("Gus runs") == "Gs rns"
    assert shorten("Bud jumps") == "Bd jmps"
def test_all():
    assert shorten("Sam went to visit Bob") == "Sm wnt t vst Bb"
    assert shorten("Tim and Gus run home") == "Tm nd Gs rn hm"
def test_number():
    assert shorten("Hello 123") == "Hll 123"
def test_punctuation():
    assert shorten("Hello! How are you doing?") == "Hll! Hw r y dng?"
def test_capitalised():
    assert shorten("HELLO HOW ARE YOU! Great!") == "HLL HW R Y! Grt!"
