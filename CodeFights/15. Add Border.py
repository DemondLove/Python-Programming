'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1.
'''

def addBorder(picture):
    stringLength = len(picture[0])
    li = []
    for i in range(len(picture)+1):
        print(i)
        if i == 0:
            picture.insert(0, '*'*(stringLength+2))
        else:
            picture[i] = '*'+picture[i]+'*'
    
    picture.insert(len(picture)+1, '*'*(stringLength+2))
    
    return picture
