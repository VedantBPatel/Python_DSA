class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def is_leaf(node):
    return node and not node.left and not node.right

def add_left_boundry(root,res):
    if not root or is_leaf(root):
        return
    
    res.append(root.data)
    if root.left:
        add_left_boundry(root.left,res)
    elif root.right:
        add_left_boundry(root.right,res)


def add_right_boundry(root,res):
    if not root or is_leaf(root):
        return
    
    if root.right:
        add_right_boundry(root.right,res)
    
    elif root.left:
        add_right_boundry(root.left,res)
    res.append(root.data)


def add_leaf_nodes(root,res):
    if not root:
        return
    if is_leaf(root):
        res.append(root.data)
    add_leaf_nodes(root.left,res)
    add_leaf_nodes(root.right,res)

def print_boundry(root):
    if not root:
        return
    res=[]
    
    res.append(root.data)

    add_left_boundry(root.left,res)
    add_leaf_nodes(root.left,res)
    add_leaf_nodes(root.right,res)
    add_right_boundry(root.right,res)
    return res

if __name__ == "__main__":
    # Construct the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.right.left = Node(7)
    root.left.right.right = Node(8)
    root.right.right = Node(9)
    root.right.right.left = Node(10)

    # Perform boundary traversal and print the result
    result = print_boundry(root)
    print("Boundary Traversal:", result)