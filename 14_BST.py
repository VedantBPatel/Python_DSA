class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a value into the BST
def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)  # Create a new node if root is empty
    
    if value < root.data:
        # Insert into the left subtree
        root.left = insert_into_bst(root.left, value)
    elif value > root.data:
        # Insert into the right subtree
        root.right = insert_into_bst(root.right, value)
    
    return root  # Return the updated root

# Function to perform Inorder Traversal (sorted order)
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Driver code to create and test the BST
if __name__ == "__main__":
    # Example: Insert nodes into the BST
    values = [10, 5, 15, 3, 7, 12, 18]
    root = None
    for value in values:
        root = insert_into_bst(root, value)

    print("Inorder traversal of the BST:")
    inorder_traversal(root)
    print()
"""
# Step-by-Step Breakdown of `insert_into_bst` Function

# Inserting values into an initially empty BST: [10, 5, 15, 3, 7, 12, 18]

### Iteration 1: Insert 10
- Current root: None (Tree is empty).
- Create a new node with value 10.
- Return this new node as the root.

Tree after this iteration:
    10

---

### Iteration 2: Insert 5
- Current root: 10
- Compare 5 with 10:
    - 5 < 10 → Move to left subtree (root.left = None).
- Create a new node with value 5.
- Assign this node to root.left (left child of 10).
- Return root (10), now updated with left child 5.

Tree after this iteration:
    10
   /
  5

---

### Iteration 3: Insert 15
- Current root: 10
- Compare 15 with 10:
    - 15 > 10 → Move to right subtree (root.right = None).
- Create a new node with value 15.
- Assign this node to root.right (right child of 10).
- Return root (10), now updated with right child 15.

Tree after this iteration:
    10
   /  \
  5    15

---

### Iteration 4: Insert 3
- Current root: 10
- Compare 3 with 10:
    - 3 < 10 → Move to left subtree (root.left = 5).
- Current root: 5
- Compare 3 with 5:
    - 3 < 5 → Move to left subtree (root.left = None).
- Create a new node with value 3.
- Assign this node to root.left (left child of 5).
- Return root (5), now updated with left child 3.
- Return root (10), now updated with the updated left subtree.

Tree after this iteration:
       10
      /  \
     5    15
    /
   3

---

### Iteration 5: Insert 7
- Current root: 10
- Compare 7 with 10:
    - 7 < 10 → Move to left subtree (root.left = 5).
- Current root: 5
- Compare 7 with 5:
    - 7 > 5 → Move to right subtree (root.right = None).
- Create a new node with value 7.
- Assign this node to root.right (right child of 5).
- Return root (5), now updated with right child 7.
- Return root (10), now updated with the updated left subtree.

Tree after this iteration:
       10
      /  \
     5    15
    / \
   3   7

---

### Iteration 6: Insert 12
- Current root: 10
- Compare 12 with 10:
    - 12 > 10 → Move to right subtree (root.right = 15).
- Current root: 15
- Compare 12 with 15:
    - 12 < 15 → Move to left subtree (root.left = None).
- Create a new node with value 12.
- Assign this node to root.left (left child of 15).
- Return root (15), now updated with left child 12.
- Return root (10), now updated with the updated right subtree.

Tree after this iteration:
       10
      /  \
     5    15
    / \   /
   3   7 12

---

### Iteration 7: Insert 18
- Current root: 10
- Compare 18 with 10:
    - 18 > 10 → Move to right subtree (root.right = 15).
- Current root: 15
- Compare 18 with 15:
    - 18 > 15 → Move to right subtree (root.right = None).
- Create a new node with value 18.
- Assign this node to root.right (right child of 15).
- Return root (15), now updated with right child 18.
- Return root (10), now updated with the updated right subtree.

Tree after this iteration:
       10
      /  \
     5    15
    / \   / \
   3   7 12  18

---
"""
### **Final BST**
