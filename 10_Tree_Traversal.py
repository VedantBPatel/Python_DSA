class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createNode(value):
    return TreeNode(value)

def PreorderTraversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    PreorderTraversal(root.left)
    PreorderTraversal(root.right)

def InorderTraversal(root):
    if root is None:
        return
    InorderTraversal(root.left)
    print(root.data, end=" ")
    InorderTraversal(root.right)

def PostorderTraversal(root):
    if root is None:
        return
    PostorderTraversal(root.left)
    PostorderTraversal(root.right)
    print(root.data, end=" ")

if __name__=="__main__":
    root = createNode(1)
    root.left = createNode(2)
    root.right = createNode(3)
    root.left.left = createNode(4)
    root.left.right = createNode(5)
    root.right.left = createNode(6)
    root.right.right = createNode(7)
    root.right.right.right = createNode(8)
    
    print("Preorder traversal: ")
    PreorderTraversal(root)
    print()

    print("Inorder traversal: ")
    InorderTraversal(root)
    print()

    print("Postorder traversal: ")
    PostorderTraversal(root)
    print()