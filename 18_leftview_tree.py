class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def left_Side_View(root):
    result=[]

    def recursion(node,level):
        if not node:
            return
        
        if level==len(result):
            result.append(node)

        recursion(node.left,level+1)
        recursion(node.right,level+1)
    
    recursion(root,0)
    return result

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.left.right.left=Node(8)
    root.left.right.right=Node(9)
    root.right.right.right=Node(10)
