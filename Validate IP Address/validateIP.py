def validateIP(ip):
  
  "aaaaaaaaaaaaaa...."
  
  numbers_list = ip.split(".")  
  # "X.X.X.X"["X", "X", "X", "X"]
  #  X -> [0, 255]
  if len(numbers_list) != 4: 
    return False 
  
  for i in range(len(numbers_list)):
    if not (isValid(numbers_list[i])): 
      return False
  
  return True 
 

def isValid(myNumber):
  if not (isNumber(myNumber)): 
    return False 
  
  myNumber = int(myNumber)
  if(myNumber >= 0 and myNumber <= 255):
    return True 
  return False 


def isNumber(myString):
  if(len(myString) == 0):
    return False
  # mySting = "12A"
  zero_ascii = ord('0') # ascii value of 0 
  nine_ascii = ord('9')
  
  for i in myString:
    if not (ord(i)>= zero_ascii and ord(i) <= nine_ascii):
      return False 
  
  return True 
      
ip = "1..23.4" # 1, "", 23, 4

print(validateIP(ip))