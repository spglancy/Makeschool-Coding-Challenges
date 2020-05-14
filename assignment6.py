# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.
def reverseTree(root):
  if (root == None) 
  return None

  temp = root.right
  root.right = root.left
  root.left = temp

  reverseTree(root.left)
  reverseTree(root.right)
