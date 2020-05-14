# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
def twosum(arr1, arr2, t):
  best = 0
  arr2.sort()
  for i in arr1:
    closest = binary_search(arr2, t-i)
    if t-(closest+i) < t-(best[0]+best[1]):
      best = (closest, i)
  return best

def binary_search(arr, target):

  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  if target == arr[mid] or len(arr) == 1:
    return arr[mid]
  elif target > arr[mid]:
    return binary_search(right, target)
  elif target < arr[mid]:
    return binary_search(left, target)