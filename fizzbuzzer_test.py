from fizzbuzzer import robot


def test_robot_1_is_not_multiple_of_3_and_5():
    assert robot(1) == "1"

def test_robot_2_is_not_multiple_of_3_and_5():
    assert robot(2) == "2"

def test_robot_4_is_not_multiple_of_3_and_5():
    assert robot(4) == "4"

def test_robot_3_is_multiple_of_3():
    assert robot(3) == "fizz"

def test_robot_6_is_multiple_of_3():
    assert robot(6) == "fizz"

def test_robot_9_is_multiple_of_3():
    assert robot(9) == "fizz"

def test_robot_5_is_multiple_of_5():
    assert robot(5) == "buzz"

def test_robot_10_is_multiple_of_5():
    assert robot(10) == "buzz"

def test_robot_20_is_multiple_of_5():
    assert robot(20) == "buzz"

def test_robot_15_is_multiple_of_5_and_3():
    assert robot(15) == "fizzbuzz"

def test_robot_30_is_multiple_of_5_and_3():
    assert robot(30) == "fizzbuzz"

def test_robot_45_is_multiple_of_5_and_3():
    assert robot(45) == "fizzbuzz"