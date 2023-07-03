#Problem: https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        mun =num[::-1]
        if(num==mun):
            return True
        else:
            return False
