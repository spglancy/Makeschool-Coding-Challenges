# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
def twoSum(nums, target):
        for index1, val1 in enumerate(nums):
            for index2, val2 in enumerate(nums):
                if val1 + val2 == target and index1 != index2:
                    return [index1, index2]

def twoSum2(nums, target):
  newDict = {}
  for index, i in enumerate(nums):
    if i in newDict:
      newDict[i].push(index)
    else:
      newDict[i] = [index]
  for index, i in enumerate(nums):
    if target-i in newDict:
      return [index, newDict[target-i][0]]

print(twoSum2([1, 2, 3, 4, 5], 7))