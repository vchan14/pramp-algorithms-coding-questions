def absSort(arr):
  abs_array = []
  
  for i in range(len(arr)):
    if arr[i] < 0: 
      abs_array.append([arr[i] * -1, -1])
    elif arr[i] > 0:
      abs_array.append([arr[i], 1])
    else:
      abs_array.append([0, 1])
  
  min_index = 0
  for i in range(len(abs_array)):
    min_index = i 
    for j in range(i+1, len(abs_array)):
      if abs_array[min_index][0] > abs_array[j][0]:
        min_index = j
      elif abs_array[min_index][0] == abs_array[j][0]:
        if abs_array[min_index][1] > abs_array[j][1]:
          min_index = j 
    abs_array[min_index], abs_array[i] = abs_array[i], abs_array[min_index]
    
    #print("Swap {} with {}". format(abs_array[min_index], abs_array[j]))
  
  result = []
  for i in range(len(abs_array)):
    result.append(abs_array[i][0] * abs_array[i][1])
  return result