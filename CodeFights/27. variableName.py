'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string name

Guaranteed constraints:
1 ≤ name.length ≤ 10.

[output] boolean

true if name is a correct variable name, false otherwise.
'''

def variableName(name):
    if name[0] not in ['0','1','2','3','4','5','6','7','8','9']:
        for x in name:
            if not x.isalnum() and x not in ['_']:
                return False
        return True
    else:
        return False
