class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        # store num : index
        #  our answer is the index of the matching numbers so index will be the value in k,v pair

        #  enumerate to get index for each num, workout differnce from current num and the target 
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        # if the difference is already in prevmap then return list of the current index and the index stored as value in prevmap
        # if not we add k,v pair to our prevmap