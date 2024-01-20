class Solution:
    def rabin_karp(self, s, t):
        p = 31
        m = 10**9 + 9
        S, T = len(s), len(t)

        # Precompute powers of p
        p_pow = [1] * max(S, T)
        for i in range(1, len(p_pow)):
            p_pow[i] = (p_pow[i - 1] * p) % m

        h_s = sum((ord(s[i]) - ord('a') + 1) * p_pow[i] for i in range(S)) % m
        h = [0] * (T + 1)
        for i in range(T):
            h[i + 1] = (h[i] + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % m
            
        occurrences = []
        for i in range(T - S + 1):
            cur_h = (h[i + S] + m - h[i]) % m
            if cur_h == (h_s * p_pow[i]) % m:
                occurrences.append(i)

        return occurrences

    def beautifulIndices(self, s, a, b, k):
        a_ind = self.rabin_karp(a, s)
        b_ind = self.rabin_karp(b, s)

        ans = []
        i, j = 0, 0

        while i < len(a_ind) and j < len(b_ind):
            if abs(a_ind[i] - b_ind[j]) <= k:
                ans.append(a_ind[i])
                i += 1
            elif a_ind[i] < b_ind[j]:
                i += 1
            else:
                j += 1

        return ans

        
        
