def num_of_paths_to_dest_1(n):
  # Depth First Search 
  
  size = n 
  paths = [0]  
  dfs(0, 0 , size, paths)
  return paths[0]
  
  
def dfs(ci, cj, size, paths):
  if (ci == (size - 1) and cj == (size-1)):
    paths[0] +=1 
  # right Num
  if((ci + 1) < size): 
    dfs(ci+1, cj, size, paths)
    
  # up 
  if((cj+1) <= ci):
    dfs(ci, cj + 1, size, paths)



def num_of_paths_to_dest(n):
  dp = []
  for i in range(n):
    dp.append([0] * n)
  
  dp[0][0] = 1 
  
  for i in range(n):
    for j in range(n):
      if j <= i:
        # left 
        if(i-1 >= j):
          dp[i][j] += dp[i-1][j]
        
        if(j-1 >= 0):
          dp[i][j] += dp[i][j-1]
  print(dp)
  return dp[n-1][n-1]