class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        # set two pointers

        while l <= r:
            #  move pointers based on if combined they are less than or more thaan the target
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            # if we reach the target return pointers(index's) + 1 as question stated 
            # 'Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.'
            else:
                return [l + 1, r + 1]