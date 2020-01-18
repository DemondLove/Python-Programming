/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            goal = target-nums[i]
            if goal in nums:
                if i == nums.index(goal):
                    continue
                else:
                    if nums[i] + nums[nums.index(goal)] == target:
                        return [i, nums.index(goal)]
