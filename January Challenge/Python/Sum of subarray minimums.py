class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        st = []
        arr = [0] + arr + [0]
        res = 0
        for i in range(len(arr)):
            while st and arr[i] < arr[st[-1]]:
                curr = st.pop() 
                res += arr[curr] * (i - curr) * (curr - st[-1])
            st.append(i)
        return res % MOD
