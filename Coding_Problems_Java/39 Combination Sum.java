import java.util.ArrayList;
import java.util.List;

class Solution {
    private void helper(int start, ArrayList<Integer> path, int target, List<ArrayList<Integer>> res, int[] candidates){
        if (target < 0){
            return;
        }
        if (target == 0){
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length; i++){
            path.add(candidates[i]);
            helper(i, path, target - candidates[i], res, candidates);
            path.remove(path.size() - 1);
        }
    }
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<ArrayList<Integer>> res = new ArrayList<>(); 
        ArrayList<Integer> path = new ArrayList<>();
        helper(0, path, target, res, candidates);
        return new ArrayList<>(res);
    }
}
