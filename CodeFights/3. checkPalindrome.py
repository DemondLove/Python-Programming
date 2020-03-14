'''
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
'''

def checkPalindrome(inputString):
    li = [x for x in inputString]
    
    midIdx = len(li)//2
    
    firstHalf = li[:midIdx]    
    
    if len(li)%2 == 0:
        secondHalf = li[midIdx:]
    else:
        secondHalf = li[midIdx+1:]
        
    secondHalf.reverse()

    if firstHalf == secondHalf:
        return True
    else:
        return False
