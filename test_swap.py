from swap import swap

def test_case1():
    result = swap(10, 12)
    print("Result of test_case1:", result)
    assert result == (12, 10)

def test_case2():
    result = swap(2, 3)
    print("Result of test_case2:", result)
    assert result == (3, 2)

def test_case3():
    result = swap(4, 5)
    print("Result of test_case3:", result)
    assert result == (5, 4)

if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    print("All tests executed ✅"))  
