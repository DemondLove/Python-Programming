'''
1207. Unique Number of Occurrences
Easy

55

2

Favorite

Share
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_dict = {}
        for x in arr:
            if str(x) not in list(unique_dict.keys()):
                unique_dict[str(x)] = 1
            else:
                unique_dict[str(x)] = unique_dict[str(x)]+1

        if len(unique_dict.values()) == len(set(unique_dict.values())):
            return True
        else:
            return False