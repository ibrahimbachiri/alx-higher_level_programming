#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.
"""

import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the left side of the current column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """Solve the N-Queens puzzle for a given board size (n x n)."""
    board = [[0] * n for _ in range(n)]
    solutions = []

    def solve(row):
        if row == n:
            solutions.append([[i, j] for i in range(n) for j in range(n) if board[i][j] == 1])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a valid integer greater than or equal to 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

    print(f"Found {len(solutions)} solutions")
    sys.exit(0)
