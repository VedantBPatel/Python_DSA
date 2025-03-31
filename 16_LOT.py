class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return  # Base case: empty tree

    queue = [root]  # Initialize the queue with the root node

    while queue:
        # Get the node at the front of the queue
        temp_Node = queue.pop(0)
        
        # Print the value of the current node
        print(temp_Node.data, end=" ")

        # Add the left child to the queue (if it exists)
        if temp_Node.left:
            queue.append(temp_Node.left)

        # Add the right child to the queue (if it exists)
        if temp_Node.right:
            queue.append(temp_Node.right)

if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Level Order Traversal of Binary Tree:")
    levelOrder(root)

"""
| Iteration | Queue State         | Processed Node| Output     |
|-----------|---------------------|---------------|------------|
| 1         | [1]                | 1              | 1          |
| 2         | [2, 3]             | 2              | 1 2        |
| 3         | [3, 4, 5]          | 3              | 1 2 3      |
| 4         | [4, 5, 6]          | 4              | 1 2 3 4    |
| 5         | [5, 6]             | 5              | 1 2 3 4 5  |
| 6         | [6]                | 6              | 1 2 3 4 5 6|
| 7         | [] (Empty)         | -              | -          |

"""