# Problem: https://leetcode.com/problems/power-of-two/description/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<= 0:
            return False
        if n==1:
            return True
        while (n%2==0):
            n/=2
        return n==1
