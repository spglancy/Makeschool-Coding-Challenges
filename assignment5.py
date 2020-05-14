# Fully solve at least two of the below linked lists problems in real working code. Use your idea sketches and pseudocode from class, type it in your code editor, run some test cases, and debug your code so it works correctly. Implement at least one solution for 2 or more of the problems below.

# Given a singly-linked list, find the middle value in the list.
# Example: If the given linked list is A → B → C → D → E, return C.
# Assumptions: The length (n) is odd so the linked list has a definite middle.

def findMiddle(ll):
  middle = ll.head
  count = 1
  lead = ll.head
  while(lead.next is not None):
    lead = lead.next
    count += 1
  for(i in range(count/2)):
    middle = middle.next
  return middle


# Given a singly-linked list, reverse the order of the list by modifying the nodes’ links.
# Example: If the given linked list is A → B → C → D → E, nodes should be modified/rearranged so the list becomes E → D → C → B → A.
def revll(ll):
  lead = ll.head
  prev = None
  post = None
  while(lead.next is not None):
    prev = lead
    lead = lead.next
    post = lead.next
    lead.next = prev
    lead = post
