class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n not in hashset:
            hashset.add(n)
            n = self.squarenum(n)
            if n == 1:
                return True
        return False

    def squarenum(self, n):
        total = 0
        while n:
            
            digit = n%10
            total += digit ** 2
            n = n // 10
        return total
