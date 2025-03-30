class ListNode:
  def __init__(self,val,next=None):
    self.val=val
    self.next=next
    
def mergeTwoLists(l1,l2):
  if l1 is None:
    return l2
  if l2 is None:
    return l1
    
  if l1.val<=l2.val:
    l1.next=mergeTwoLists(l1.next,l2)
    return l1
  else:
    l2.next=mergeTwoLists(l1,l2.next)
    return l2
  
def print_list(head):
  current =head
  while current:
    print(current.val, end= " ")
    current=current.next
  print("NULL")
    
if __name__=="__main__":
  l1 =ListNode(1)
  l1.next = ListNode(3)
  l1.next.next = ListNode(5)
  
  l2 = ListNode(2)
  l2.next = ListNode(4)
  l2.next.next = ListNode(6)
  
  print("List 1: ")
  print_list(l1)
  
  print("List 2: ")
  print_list(l2)
  
  merged_list = mergeTwoLists(l1,l2)
  print("Merged list: ")
  print_list(merged_list)