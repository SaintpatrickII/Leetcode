class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #  ensure that if we are at index > 0 and the number is the same as prev num that we skip
            if i > 0 and a == nums[i - 1]:
                continue
            # first val is i, so left -> right is num after i and end of nums
            l, r = i + 1, len(nums) - 1
            while l < r:
                # check if sum is above, below or = 0, if equal add to res
                if a + nums[l] + nums[r] > 0:
                    r -= 1
                elif a + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    # if its equal we also shift left pointer to see if any other soln's can be found for same index
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res