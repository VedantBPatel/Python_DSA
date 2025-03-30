class Node:
  def __init__(self,val):
    self.val=val
    self.next=None
    
def SwapPairs(head):
  dummy = Node(0)
  dummy.next = head
  point = dummy
  
  while point.next and point.next.next:
    s1 = point.next
    s2 = point.next.next
    
    s1.next = s2.next
    s2.next = s1
    
    point.next = s2
    point = s1
    
  return dummy.next
  
def print_list(head):
  while head:
    print(head.val, end=" -> ")
    head = head.next
  print("NULL")
  
if __name__ =="__main__":
  l = Node(1)
  l.next = Node(2)
  l.next.next = Node(3)
  l.next.next.next = Node(4)
  l.next.next.next.next = Node(5)
  
  print("Original List: ")
  print_list(l)
  
  result = SwapPairs(l)
  
  print("After swap pairwise:")
  print_list(result)