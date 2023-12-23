class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null){
            return res;
        }

        queue.offer(root);
        while(!queue.isEmpty()){
            int level = queue.size();
            ArrayList<Integer> temp = new ArrayList<>();
            for (int i = 0; i < level; i++){
                TreeNode curr_ele = queue.poll();
                temp.add(curr_ele.val);

                if (curr_ele.left != null){
                    queue.offer(curr_ele.left);
                }

                if (curr_ele.right != null){
                    queue.offer(curr_ele.right);
                }
            }
            double value = temp.stream().mapToInt(Integer::intValue).average().orElse(0.0);
            res.add(value);
        }

        return res;
    }
}
