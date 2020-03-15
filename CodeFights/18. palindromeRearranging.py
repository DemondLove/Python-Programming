'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
'''

def palindromeRearranging(inputString):
    strDict = {}
    for x in inputString:
        if x not in strDict.keys():
            strDict[x] = 1
        else:
            strDict[x] = strDict[x]+1
    
    oddTerms = 0
    for x in strDict.keys():
        if strDict[x]%2 != 0:
            oddTerms+=1
    
    if oddTerms > 1:
        return False
    else:
        return True
