class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def createNode(data):
    return TreeNode(data)

def find_depth(root):
    if root is None:
        return 0
    leftDepth=find_depth(root.left)
    rightDepth=find_depth(root.right)
    return max(leftDepth,rightDepth)+1

if __name__=="__main__":
    root=createNode(1)
    root.left=createNode(2)
    root.right=createNode(3)
    root.left.left=createNode(4)
    root.left.right=createNode(5)
    root.right.right=createNode(6)
    root.right.right.right=createNode(7)
    depth=find_depth(root)
    print(f"The depth of the tree is: {depth}")

"""
find_depth(1)
├── find_depth(2)
│   ├── find_depth(4) → 1
│   └── find_depth(5) → 1
│       → max(1, 1) + 1 = 2
├── find_depth(3)
│   ├── find_depth(None) → 0
│   └── find_depth(6)
│       ├── find_depth(None) → 0
│       └── find_depth(7) → 1
│           → max(0, 1) + 1 = 2
│       → max(0, 2) + 1 = 3
→ max(2, 3) + 1 = 4

"""