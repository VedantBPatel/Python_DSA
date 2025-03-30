class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def createNode(data):
    return TreeNode(data)

def are_Mirrored(root1,root2):
    if root1==None and root2==None:#when trees are empty
        return True
    
    if root1==None or root2==None:#when one of the tree is empty
        return False
    
    return(root1.data==root2.data and are_Mirrored(root1.left,root2.right) and are_Mirrored(root1.right,root2.left))
if __name__=="__main__":
    t1=createNode(10)
    t1.left=createNode(20)
    t1.right=createNode(30)

    t2=createNode(10)
    t2.left=createNode(30)
    t2.right=createNode(20)

    if are_Mirrored(t1,t2):
        print("Both Trees are mirrored.\n")
    else:
        print("Both Trees are not mirrored.\n")