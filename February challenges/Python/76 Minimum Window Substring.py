class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, windowT = {}, {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        have, need = 0, len(countT)
        resLen = float("infinity")
        res = [-1, -1]
        l = 0
        for r in range(len(s)):
            c = s[r]
            windowT[c] = 1 + windowT.get(c, 0)

            if c in countT and windowT[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                windowT[s[l]] -= 1
                if s[l] in countT and windowT[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
 

            
