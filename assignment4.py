# Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.

# What clarifying questions would you ask?
# What do you mean by counterclockwise

# What reasonable assumptions could you state?
# Ill assume that I have the head and the tail of the LL and that the nodes are connected via .next

# What are 2-3 ways you can simplify the problem?
# I start thinking of it as removing a node and replacing it where it should go

# Brainstorm 2-3 ways to approach the problem.
# 1. skip to the kth node and set that to the tails .next and then set it to tail and go from there. 2. go through each node moving it from the first node.

# Choose one idea and write pseudocode for it.
# save the K+1th and Kth node in a var
# set the tails .next to the head
# set the K+1th var node to the head
# set the tail to the Kth node and remove its .next

rotate(ll, k):
  kthnode = ll.head
  for i in range(k):
    kthnode = kthnode.next
  newhead = kthnode.next
  ll.tail.next = ll.head
  ll.head = newhead
  ll.tail = kthnode
  kthnode.next = null
