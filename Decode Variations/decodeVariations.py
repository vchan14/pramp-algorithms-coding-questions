def decodeVariations(S):
  if S is None or len(S) ==0 or S[0] == 0:
    return 0
  
  dp = [0] * (len(S))
  # base cases 
  dp[0] = 1 
  if len(S) > 1: 
    if int(S[1]) != 0 and int(S[0:2]) <= 26: 
      dp[1] = 2
    else:
      dp[1] = 1
  
  for i in range(2,len(S)):
    if int(S[i]) != 0: 
      dp[i] += dp[i-1]
    if int(S[(i-1):(i+1)]) <= 26 and int(S[(i-1):(i+1)]) >= 10:
      dp[i] += dp[i-2]
  
  return dp[len(S)-1]
  


def decodeVariations_2(S):
  dp = [0] * len(S)
  
  if(S == None or len(S) == 0):
    return -1
  
  if(len(S) == 1):
    if(S[0] != '0'):
      return 1
  
  if(len(S) >= 2):
    if S[0] == '0':
      return -1
    else:
      dp[0] = 1
    if int(S[0:2]) <= 26:
      dp[1] = 2
    else: 
      dp[1] = 1
  for i in range(2, len(S)):
    if int(S[i]) != 0:
      dp[i] = dp[i-1]
    if int(S[i-1]) !=0:
      if int(S[i-1 : i+1]) <= 26:
        print(S[i-1 : i+1])
        dp[i] += dp[i-2]
  
  return dp[len(S) -1]
    