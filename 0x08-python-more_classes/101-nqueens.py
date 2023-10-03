#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col == n:
            solutions.append([[i, row] for i, row in enumerate(board)])
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                backtrack(col + 1)
                board[i][col] = 0

    backtrack(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError()
    except ValueError:
        print("N must be a number and at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
