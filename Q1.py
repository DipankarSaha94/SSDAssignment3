def answer(data):
  name = []
  parent = []
  for key1, value1 in data.items():
    for item in value1:
      for key2,value2 in item.items():
        if key2 == 'name':
          name.append(value2)
        if key2 == 'parent':
          parent.append(value2)
  name.pop(0)

  input1,input2 = map(str,input().split())

  parent1 = []
  try:
    index1 = name.index(input1)
  except ValueError:
    print(input1 +' , '+ input2+" Doesn't have a common leader")
    return
  while True:
    parent1.append(parent[index1])
    try:
      index1 = name.index(parent[index1])
    except ValueError:
      break

  parent2 = []
  try:
    index2 = name.index(input2)
  except ValueError:
    print(input1 +' , '+ input2+" Doesn't have a common leader")
    return

  while True:
    parent2.append(parent[index2])
    try:
      index2 = name.index(parent[index2])
    except ValueError:
      break
  
  
  
  level1 = 0
  for i in parent2:
    level1 += 1 
    level2 = 0
    for j in parent1:
      level2 += 1
      if i == j:
        print(i)
        print(i + " is " + str(level1) + " levels above than " + input2)
        print(i + " is " + str(level2) + " levels above than " + input1)
        return

  print(input1 +' , '+ input2+" Doesn't have a common leader") 


#driver code 
import json

with open('/home/dipankar/Desktop/Assignment3/org.json') as f:
  data = json.load(f)

answer(data)
