from challenge3 import solution

def test_solution():
    assert solution(52) == 'aa' + 'b'*2 + 'c'*2 + 'd'*2 + 'e'*2 + 'f'*2 + 'g'*2 + 'h'*2 + 'i'*2 + 'j'*2 + 'k'*2 + 'l'*2 + 'm'*2 + 'n'*2 + 'o'*2 + 'p'*2 + 'q'*2 + 'r'*2 + 's'*2 + 't'*2 + 'u'*2 + 'v'*2 + 'w'*2 + 'x'*2 + 'y'*2 + 'z'*2
    assert solution(27) == 'aa' + 'b' + 'c' + 'd' + 'e' + 'f' + 'g' + 'h' + 'i' + 'j' + 'k' + 'l' + 'm' + 'n' + 'o' + 'p' + 'q' + 'r' + 's' + 't' + 'u' + 'v' + 'w' + 'x' + 'y' + 'z'
    assert solution(0) == ''