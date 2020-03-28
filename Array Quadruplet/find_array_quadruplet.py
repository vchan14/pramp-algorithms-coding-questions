
import collections
def find_array_quadruplet(arr, s):
  arr.sort()
  myTable = {}
  for i in arr: 
    if i in myTable:
      myTable[i] +=1
    else:
      myTable[i] = 1
  
  for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
      for k in range(j+1, len(arr)): 
        myTable[arr[i]] -= 1
        myTable[arr[j]] -= 1
        myTable[arr[k]] -= 1
        mySum = s - (arr[i] + arr[j] + arr[k])
        if mySum in myTable and myTable[mySum] > 0:
          return [arr[i], arr[j], arr[k], mySum]
        
        myTable[arr[i]] += 1
        myTable[arr[j]] += 1
        myTable[arr[k]] += 1
  
  return []
        
  

      
      

