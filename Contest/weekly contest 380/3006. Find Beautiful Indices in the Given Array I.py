class Solution(object):
    def beautifulIndices(self,s, a, b, k):
        a_ind = []
        b_ind = []
        ans = []
        x, y= len(a), len(b)
        for i in range(len(s)):
            if s[i:i+x] == a:
                a_ind.append(i)
            if s[i:i+y] == b:
                b_ind.append(i)

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
        
