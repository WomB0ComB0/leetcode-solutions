class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<Integer> currentPath = new ArrayList(); // current path
        List<List<Integer>> allPaths = new ArrayList(); // all paths
        findPathsRecursive(root, targetSum, currentPath, allPaths); // find all paths
        return allPaths;
    }
    private static void findPathsRecursive(TreeNode currentNode, int sum, List<Integer> currentPath, List<List<Integer>> allPaths){
        if(currentNode == null) return;
        currentPath.add(currentNode.val); // add current node to the path
        if (currentNode.val == sum && currentNode.left == null && currentNode.right == null) { // if the current node is a leaf and its value is equal to sum, save the current path
            allPaths.add(new ArrayList<Integer>(currentPath)); // add current path to all paths
        } else {
            findPathsRecursive(currentNode.left, sum - currentNode.val, currentPath, allPaths); // traverse left subtree
            findPathsRecursive(currentNode.right, sum - currentNode.val, currentPath, allPaths); // traverse right subtree
        }
        currentPath.remove(currentPath.size()-1); // remove current node from the path to backtrack, we need to remove the current node while we are going up the recursive call stack.
    }
    public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
    }
}