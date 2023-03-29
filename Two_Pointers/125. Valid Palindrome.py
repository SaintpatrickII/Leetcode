class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for c in s:
            if c .isalnum():
                new_str += c.lower()
        # create new string, only accept alphanumeric chars, & make them all lowercase


        #  left pointer at 0 and right at end of string
        l, r = 0, len(new_str) - 1

        #  condition while left & right pointers havent passed wach other
        while l <= r:
            #  check chars are same at each pointer, return false if not
            if new_str[l] != new_str[r]:
                return False
            #  move pointers inwards
            l += 1
            r -= 1
        #  if loop exits with no false statement return true
        return True