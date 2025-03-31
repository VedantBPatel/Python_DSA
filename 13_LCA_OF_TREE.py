class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def LCA(root,n1,n2):
    if root is None or root.data==n1 or root.data==n2:
        return root
    left_lca=LCA(root.left,n1,n2)
    right_lca=LCA(root.right,n1,n2)

    if left_lca is not None and right_lca is not None:
        return root
    
    
    return left_lca if left_lca is not None else right_lca

if __name__=="__main__":
    root=TreeNode(3)
    root.left=TreeNode(5)
    root.right=TreeNode(1)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)
    root.right.left=TreeNode(0)
    root.right.right=TreeNode(8)
    root.left.right.left=TreeNode(7)
    root.left.right.right=TreeNode(4)

    n1=7
    n2=4
    lca=LCA(root,n1,n2)
    print(f"LCA of {n1} and {n2} is: {lca.data if lca else 'None'}")

"""
                3
              /   \
             5     1
            / \   / \
           6   2 0   8
              / \
             7   4

"""

# Explanation
"""
1. TreeNode Class:
   - Represents a single node in the binary tree with a value (data) and pointers to its left and right children.

2. LCA Function:
   - Uses recursion to find the Lowest Common Ancestor (LCA) of two nodes in a binary tree.
   - Base Case:
     - If the current node is None, return None.
     - If the current node matches either of the target nodes (n1 or n2), return the current node as a potential LCA.
   - Recursive Calls:
     - Recursively search for LCA in the left and right subtrees.
     - If both subtrees return a non-None value, the current node is the LCA because one node is in each subtree.
     - Otherwise, return the non-None result from one of the subtrees.

3. Tree Construction:
   - Constructs the following binary tree:
       3
     /   \
    5     1
   / \   / \
  6   2 0   8
     / \
    7   4

4. Example Execution:
   - For n1 = 7 and n2 = 4:
     - Traverse the tree using the LCA function.
     - Both nodes (7 and 4) are found in the left subtree of node 2.
     - Node 2 is their Lowest Common Ancestor (LCA).
   - Output: LCA of 7 and 4 is: 2
"""