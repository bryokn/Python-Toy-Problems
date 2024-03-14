import pytest
from challenge1 import solution

def test_solution():
    assert (solution([7, 15, 10, 8]) == 13)

if __name__ == '__main__':
    pytest.main()
