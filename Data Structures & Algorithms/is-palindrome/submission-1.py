class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c for c in s if c.isalnum())

        low = s.lower()

        left = 0
        right = len(low) - 1

        while (left < right):
            if low[left] == low[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True


        