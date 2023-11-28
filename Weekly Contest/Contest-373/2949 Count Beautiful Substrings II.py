class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        if(n ==1): return 0
        p = 0
        for i in range(n,0,-1): 
            if (i*i)%k ==0: p = i
        p*=2
        
        B = [[] for _ in range(p)]
        B[p-1].append(0)
        pref = list(accumulate([1 if c in "aeiou" else 0 for c in s ]))
        
        for i in range(n):
            B[i%p].append(pref[i])
            
        ans = 0
        for i in range(p):
            cnt = Counter()
            
            for j in range(len(B[i])):
                cnt[B[i][j]-((p//2)*j)]+=1
                    
            for x in cnt.values():
                ans+=(x*(x-1))//2
                    
        return ans
