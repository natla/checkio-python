"""
Chess is a two-player strategy game played on a checkered game board laid out in eight rows
(called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h).
Each square of the chessboard is identified by a unique coordinate pair — a letter and a number
(ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture
an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square.
For white pawns the front squares are squares with greater row number than the square they currently occupy.

With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns. You should design your code to find
how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Precondition:
0 < pawns ≤ 8
"""


def safe_pawns(pawns: set) -> int:
    # A list of pawns that have already been saved by another pawn
    saved = []
    # An int to keep track of safe pawns
    results = 0
    for pawn in pawns:
        for pawn2 in pawns:
            # Check if pawn2 is placed on an adjacent file and stands on the row behind
            # Make sure the current pawn is not already placed in the saved list
            if (ord(pawn2[0]) == ord(pawn[0]) + 1 or ord(pawn2[0]) == ord(pawn[0]) - 1) and \
                    (int(pawn2[1]) == int(pawn[1]) - 1) and pawn not in saved:
                results += 1
                saved.append(pawn)
    return results

if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")