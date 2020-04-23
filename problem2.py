# Given an array a of n numbers and a count k find the k largest values in the array a.
def klargest1(nums, k):
  nums.sort(reverse=True)
  output = []
  for i in range(k):
    output.append(nums[i])
  return output

def klargest(nums, k):
  nums.sort()
  output = []
  for i in range(k):
    output.append(nums[len(nums)-i-1])
  return output

print(klargest([1,2,3,4,5,6,7,8], 3))