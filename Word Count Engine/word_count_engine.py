def word_count_engine(document):
  
  document = document.lower()

  document = list(document)
  for i in range(len(document)):
    if not (ord(document[i]) >= ord('a') and ord(document[i]) <= ord('z')):
      if document[i] != " ":
        document[i] = ""
  document = "".join(document)
  document = document.split()
  

  myDict = {}
  
  for i in range(len(document)):
    if document[i] not in myDict:
      myDict[document[i]] = [1, i * -1] 
    else:
      myDict[document[i]][0] += 1
  
  document = []
  for key, value in myDict.items():
    document.append([key, value])
  
  document = sorted(document, key = lambda x: (x[1][0], x[1][1]), reverse=True )
  output = []
  
  for i in range(len(document)):
    output.append([document[i][0], str(document[i][1][0])])
  
  
  return output 



document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))
            
  