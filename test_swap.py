from swap import swap

def test_case1():
    assert swap(10, 12) == (12, 10)

def test_case2():
    assert swap(2, 3) == (3, 2)

def test_case3():
    assert swap(4, 5) == (5, 4)  
