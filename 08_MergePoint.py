class Node:
  def __init__(self,data):
    self.data=data
    self.next=None 
    
def length(head):
  length=0
  while head:
    length += 1
    head=head.next
  return length
  
def FindMergePoint(A, B):
  len_A = length(A)
  len_B = length(B)
  d = len_B - len_A
  
  if len_A > len_B:
    A, B = B, A
    d = len_B - len_A
    
  for _ in range(d):
    B = B.next
    
  while A and B :
    if A==B:
      return A
    A = A.next
    B = B.next
  return None

if __name__ =="__main__":
  l1=Node(4)
  l1.next = Node(6)
  l1.next.next = Node(7)
  l1.next.next.next = Node(1)
  
  l2 = Node(9)
  l2.next = Node(3)
  l2.next.next= Node(5)
  l2.next.next.next = l1.next.next
  
  merged_point = FindMergePoint(l1, l2)
  
  if merged_point is None:
    print("No merge point found")
  else:
    print(f"Merge point found at node with data : {merged_point.data}")