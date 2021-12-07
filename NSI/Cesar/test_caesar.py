from caesar import *


def test():
    assert caesar_detail("A",0) == "A"
    assert caesar_detail("Z",1) == "A"
    assert caesar_detail("Y",2) == "A"
    assert caesar_detail("A",26) == "A"
    assert caesar_detail("A",26*2) == "A"
    assert caesar_detail("A",-26) == "A"
    assert caesar_detail("A",-1) == "Z"
    assert caesar_detail("",1) == ""
    assert caesar_detail("a",1) == "a"

    assert caesar_custom_alphabet(text = "A",key = 1, alpha = "abc") == "A"
    assert caesar_custom_alphabet(text = "c",key = 1, alpha = "abc") == "a"
    assert caesar_custom_alphabet(text = "Z",key = 1, alpha = "") == "Z"
    assert caesar_custom_alphabet(text = "Z",key = 1, alpha = 123456) == "Z"
test()