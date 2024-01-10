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
    ArrayList<Integer> Q = new ArrayList<>();
    public int kthSmallest(TreeNode root, int k) {
        helper(root);
        return Q.get(k-1);
    }

    
    public void helper(TreeNode root){
            if (root == null){
                return;
            }

            helper(root.left);
            Q.add(root.val);
            helper(root.right);
        
        }
}
