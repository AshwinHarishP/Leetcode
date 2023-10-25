class Solution:
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        num = 2 ** (n - 1)
        if k <= num // 2:
            return self.kthGrammar(n - 1, k)
        
        if n % 2 == 0:
            ans = self.kthGrammar(n - 1, k - (num // 2))
            if ans == 0:
                return 1
            else:
                return 0
        else:
            return self.kthGrammar(n - 1, num - k + 1)
