'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        # Obvious solution:
        #return address.replace('.', '[.]')
        
        # Manual solution:
        new_var = address.split('.')
        
        final_str = ''
        
        for x in range(len(new_var)):
            if x == len(new_var)-1:
                final_str = final_str+new_var[x]
            else:
                final_str = final_str+new_var[x]+'[.]'
        
        return final_str
