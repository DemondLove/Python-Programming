'''
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be isBeautifulString(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be isBeautifulString(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be isBeautifulString(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.
'''

def isBeautifulString(inputString):
    inputString = list(inputString)
    
    inputString.sort()
    
    for x in list(string.ascii_lowercase):
        li = [a for a in inputString if a == x]
        curr_occurance = len(li)
        if x == 'a':
            prev_occurance = len(li)
            
            if prev_occurance == 0:
                return False
        else:
            if curr_occurance > prev_occurance:
                return False
            elif prev_occurance == 0:
                return False
            else:
                prev_occurance = curr_occurance
        if x == inputString[-1]:
            break
    return True
    
    return inputString
