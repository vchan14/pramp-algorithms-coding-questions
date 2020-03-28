def array_of_array_products(arr):
  if(len(arr) == 1):
    return []
  result = [1] * len(arr)
  left = [1] * len(arr)
  right = [1] * len(arr)
  
  for i in range(1, len(arr)):
    left[i] = arr[i-1] * left[i-1]
    
  #print("left", left)
  
  for i in range(1, len(arr)):
    right[len(arr)-1-i] *= right[len(arr)-i ] * arr[len(arr)-i]
  
  #print("right", right)
  
  
  for i in range(len(left)):
    result[i] = left[i] * right[i]
    

  return result 
arr = [2,2]
print(array_of_array_products(arr))
    
    

