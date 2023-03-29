class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
#  ensure both strings are same len

        countS, countT = {}, {}
        # create two hashmaps for counts of both str
        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c], 0)
            countT[t[c]] = 1 + countT.get(t[c], 0)
            # count.get has default value of 0 otherwise would get missing key error
            # we get the char at index c of each string & add 1 to the amount stored in hashmap
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        #  loop through countS keys, make sure the values equal in both hashmaps, if not return false
        return True
        

#  we can be very cheeky & use pythons inbuilt counter to do
# return counter(s) == counter(t)