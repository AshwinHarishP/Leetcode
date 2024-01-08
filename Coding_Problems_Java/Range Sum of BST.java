/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null){
            return 0;
        }

        int Sum = 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()){
            TreeNode curr = queue.poll();

            if (curr.val >= low && curr.val <= high){
                Sum += curr.val;
            }

            if (curr.left != null){
                queue.offer(curr.left);
            }

            if (curr.right != null){
                queue.offer(curr.right);
            }
        }
        return Sum;
    
    }
}
