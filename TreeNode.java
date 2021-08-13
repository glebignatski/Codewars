import java.lang.*;

public class TreeNode {
  TreeNode left;
  TreeNode right;
  static int c = 0;

public static int height(TreeNode root)
{
    if (root == null)
    {
        return -1;
    }
    else
    {
        return 1 + Math.max(height(root.left),height(root.right));
    }
}
  public static int countNodes(TreeNode root) {
     if (root == null) {
      return 0; // set number of node to zero if empty tree is passed
    } 
      return 1 + countNodes(root.left) + countNodes(root.right); // recursively count the number of nodes
      
  }

  public static boolean isPerfect(TreeNode root) {
    int c = countNodes(root); // retrieve number of nodes of tree
    int h = height(root);
    if (c == 0) { // base case 1 (empty tree is perfect)
      return true;
    }
    else if (c == 1) { // base case 2 (single node tree is not a perfect BT)
      return true;
    }

    double expectedHeight = (Math.log10((c * 1.0) + 1.0) / Math.log10(2.0)) - 1;
    double height = h * 1.0;

    // if issues arise, check the expected, actual, and node count values

    // System.out.println("The height of the tree is " + height + "." + " The
    // expected height was "
    // + expectedHeight + "." + " The number of nodes in the tree was " + c);

    if (expectedHeight == height) { // compare heights
                    
      return true; 
    }
    return false;
  }

  static TreeNode leaf() {
    return new TreeNode();
  }

  static TreeNode join(TreeNode left, TreeNode right) {
    return new TreeNode().withChildren(left, right);
  }

  TreeNode withLeft(TreeNode left) {
    this.left = left;
    return this;
  }

  TreeNode withRight(TreeNode right) {
    this.right = right;
    return this;
  }

  TreeNode withChildren(TreeNode left, TreeNode right) {
    this.left = left;
    this.right = right;
    return this;
  }

  TreeNode withLeftLeaf() {
    return withLeft(leaf());
  }

  TreeNode withRightLeaf() {
    return withRight(leaf());
  }

  TreeNode withLeaves() {
    return withChildren(leaf(), leaf());
  }
}