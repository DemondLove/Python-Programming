'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
'''

def commonCharacterCount(s1, s2):
    li1 = [x for x in s1]
    li2 = [x for x in s2]
    
    cnt = 0
    
    for x in li1:
        if x in li2:
            cnt+=1
            li2.remove(x)
            
    return cnt
