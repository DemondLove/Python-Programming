'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string bishop

Coordinates of the white bishop in the chess notation.

Guaranteed constraints:
bishop.length = 2,
'a' ≤ bishop[0] ≤ 'h',
1 ≤ bishop[1] ≤ 8.

[input] string pawn

Coordinates of the black pawn in the same notation.

Guaranteed constraints:
pawn.length = 2,
'a' ≤ pawn[0] ≤ 'h',
1 ≤ pawn[1] ≤ 8.

[output] boolean

true if the bishop can capture the pawn, false otherwise.
'''

def bishopAndPawn(bishop, pawn):
    dictRange = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    
    bishopLi, pawnLi = list(bishop), list(pawn)

    firstValMax = max(dictRange[bishopLi[0]],dictRange[pawnLi[0]])
    firstValMin = min(dictRange[bishopLi[0]],dictRange[pawnLi[0]])
    secondValMax = max(int(bishopLi[1]),int(pawnLi[1]))
    secondValMin = min(int(bishopLi[1]),int(pawnLi[1]))

    return firstValMax-firstValMin == secondValMax-secondValMin
