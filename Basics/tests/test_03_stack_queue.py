import pytest
from src._03_stack_queue import problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8


def test_problem_1():
    """Test Valid Parentheses"""
    result = problem_1("()")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_1("()[]{}") == True
    assert problem_1("(]") == False
    assert problem_1("") == True


def test_problem_2():
    """Test Min Stack"""
    result = problem_2()
    if result is None:
        pytest.skip("Not implemented yet")
    
    result.push(3)
    assert result.getMin() == 3
    
    result.push(2)
    assert result.getMin() == 2
    
    result.push(1)
    assert result.getMin() == 1
    
    assert result.pop() == 1


def test_problem_3():
    """Test Decode String"""
    result = problem_3("3[a]")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == "aaa"
    
    assert problem_3("2[abc]") == "abcabc"
    assert problem_3("3[a2[c]]") == "accaccacc"
    assert problem_3("a") == "a"


def test_problem_4():
    """Test Largest Rectangle in Histogram"""
    result = problem_4([2, 1, 5, 6, 2, 3])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 10
    
    assert problem_4([2, 4]) == 4
    assert problem_4([5, 5, 5]) == 15
    assert problem_4([7]) == 7


def test_problem_5():
    """Test Queue from Stacks"""
    result = problem_5()
    if result is None:
        pytest.skip("Not implemented yet")
    
    result.push(1)
    result.push(2)
    assert result.pop() == 1
    
    result.push(3)
    assert result.pop() == 2


def test_problem_6():
    """Test Daily Temperatures"""
    result = problem_6([73, 74, 75, 71, 69, 72, 76, 73])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [1, 1, 4, 2, 1, 1, 0, 0]
    
    assert problem_6([5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0]
    assert problem_6([1, 2, 3, 4, 5]) == [1, 1, 1, 1, 0]
    assert problem_6([1]) == [0]


def test_problem_7():
    """Test Recent Calls"""
    result = problem_7()
    if result is None:
        pytest.skip("Not implemented yet")
    
    assert result.ping(100) == 1
    assert result.ping(2000) == 2
    assert result.ping(3001) == 3
    
    assert result.ping(3100) == 3


def test_problem_8():
    """Test Trapping Rain Water"""
    result = problem_8([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 6
    
    assert problem_8([0, 1, 2, 3]) == 0
    assert problem_8([3, 0, 2]) == 2
    assert problem_8([1]) == 0