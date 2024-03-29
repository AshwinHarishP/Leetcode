class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(start, path, target):
            if target == 0:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  
                if candidates[i] > target:
                    break  
                helper(i+1, path + [candidates[i]], target - candidates[i])

        helper(0, [], target)
        return res
