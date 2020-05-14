def kLargest(arr, k): 
  output = []
  arr.sort(reverse = True) 
  for i in range(k): 
    output.append(arr[i])
  return output
  
arr = [1, 23, 12, 9, 30, 2, 50] 
k = 3
print(kLargest(arr, k))