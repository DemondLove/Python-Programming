'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
'''

import string
def alphabeticShift(inputString):
    alphabet = [x for x in string.ascii_lowercase]
    inputString = [x for x in inputString]
    for i in range(len(inputString)):
        alpha = alphabet.index(inputString[i])
        if alpha == 25:
            inputString[i] = 'a'
        else:
            inputString[i] = alphabet[alpha+1]
    
    return ''.join(inputString)
