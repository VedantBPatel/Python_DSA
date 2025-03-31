class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def isBST(root,min_val,max_val):
    if root is None:
            return True
    if root.data<min_val or root.data>max_val:
        return False
    return isBST(root.left,min_val,root.data-1) and isBST(root.right,root.data+1,max_val)

if __name__=="__main__":
     root=TreeNode(4)
     root.left=TreeNode(2)
     root.right=TreeNode(6)
     root.left.left=TreeNode(1)
     root.left.right=TreeNode(5)
     root.right.right=TreeNode(7)
     
     INT_MIN=float('-inf')
     INT_MAX=float('inf')

     if isBST(root,INT_MIN,INT_MAX):
          print("The given tree is BST")
     else:
          print("The given tree is not BST")