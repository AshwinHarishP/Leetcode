class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(start, path, target):
            if target < 0:
                return 

            if target == 0:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                helper(i, path + [candidates[i]], target - candidates[i])
        helper(0, [], target)
        return res
        
