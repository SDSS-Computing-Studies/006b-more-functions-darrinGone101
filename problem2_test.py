#! python3

import problem2

def test1():
    assert problem2.triangle(12,5,13) == 2
    assert problem2.triangle(3,4,4.5) == 1


def test2():
    assert problem2.triangle(-2,1,5) == 0
    assert problem2.triangle(1,1,5) == 0
