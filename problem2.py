# Given an array a of n numbers and a count k find the k largest values in the array a.
def klargest(nums, k):
  nums.sort(reverse=True)
  return nums.slice(0,k)

print(klargest([1,2,3,4,5,6,7,8], 3))