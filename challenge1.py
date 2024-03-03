def solution(A):
    target = 10
    moves = 0
    
    for i in range(len(A)):
        diff = A[i] - target
        
        if diff > 0:
            A[i] -= diff
            if i < len(A) - 1:
                A[i+1] += diff
                moves += diff
            else:
                for j in range(len(A) - 2, -1, -1):
                    move_bricks = min(diff, target - A[j])
                    A[j] += move_bricks
                    A[j+1] -= move_bricks
                    moves += move_bricks
                    diff -= move_bricks
                    if diff == 0:
                        break
                if diff > 0:
                    return -1

    return moves
