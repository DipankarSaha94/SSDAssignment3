def answer(data):
  namelist.clear()
  parentlist.clear()
  for key1, value1 in data.items():
    for item in value1:
      for key2,value2 in item.items():
        if key2 == 'name':
          namelist.append(value2)
        if key2 == 'parent':
          parentlist.append(value2)
  namelist.pop(0)

  inputlist = list(map(str,input().split()))
  inputlist.pop(0)
  if(len(inputlist) == 3):
    input1,input2,input3 = inputlist[0],inputlist[1],inputlist[2]
    findleader1(input1,input2,input3)
  elif(len(inputlist) == 4):
    input1,input2,input3,input4 = inputlist[0],inputlist[1],inputlist[2],inputlist[3]
    findleader2(input1,input2,input3,input4)
  elif(len(inputlist) == 5):
    input1,input2,input3,input4,input5 = inputlist[0],inputlist[1],inputlist[2],inputlist[3],inputlist[4]
    findleader3(input1,input2,input3,input4,input5)
  else:
    print("total input not between 3 to 5")
    return



def getplist(inp,parent):
  parent.clear()
  try:
    index1 = namelist.index(inp)
  except ValueError:
    return
  while True:
    parent.append(parentlist[index1])
    try:
      index1 = namelist.index(parentlist[index1])
    except ValueError:
      break

  
def findleader1(input1,input2,input3):  
    getplist(input1,parent1)
    getplist(input2,parent2)
    getplist(input3,parent3)
    test_list = [parent1,parent2,parent3]
    f = False
    i = ""  
    res = list(reduce(lambda i, j: i & j, (set(x) for x in test_list))) 
    if(len(res)>0):
      i = res[0]
      f = True


    l1,l2,l3 = 0,0,0
    if f:
      print(i)
      l1 = parent1.index(i)
      l1 += 1
      print(i + " is " + str(l1) + " levels above than " + input1)
      l2 = parent2.index(i)
      l2 += 1
      print(i + " is " + str(l2) + " levels above than " + input2)
      l3 = parent3.index(i)
      l3 += 1
      print(i + " is " + str(l3) + " levels above than " + input3)
    else:
      print(" No common leader")
    
def findleader2(input1,input2,input3,input4):  
    getplist(input1,parent1)
    getplist(input2,parent2)
    getplist(input3,parent3)
    getplist(input4,parent4)
    
    f = False
    i = ""
    test_list = [parent1,parent2,parent3,parent4]  
    res = list(reduce(lambda i, j: i & j, (set(x) for x in test_list))) 
    if(len(res)>0):
      i = res[0]
      f = True

    l1,l2,l3,l4 = 0,0,0,0
    if f:
      print(i)
      l1 = parent1.index(i)
      l1 += 1
      print(i + " is " + str(l1) + " levels above than " + input1)
      l2 = parent2.index(i)
      l2 += 1
      print(i + " is " + str(l2) + " levels above than " + input2)
      l3 = parent3.index(i)
      l3 += 1
      print(i + " is " + str(l3) + " levels above than " + input3)
      l4 = parent4.index(i)
      l4 += 1
      print(i + " is " + str(l4) + " levels above than " + input4)
    else:
      print(" No common leader") 
 
def findleader3(input1,input2,input3,input4,input5):  
    getplist(input1,parent1)
    getplist(input2,parent2)
    getplist(input3,parent3)
    getplist(input4,parent4)
    getplist(input5,parent5)
    
    f = False
    i = ''
    test_list = [parent1,parent2,parent3,parent5]  
    res = list(reduce(lambda i, j: i & j, (set(x) for x in test_list))) 
    if(len(res)>0):
      i = res[0]
      f = True

    l1,l2,l3,l4,l5 = 0,0,0,0,0
    if f:
      print(i)
      l1 = parent1.index(i)
      l1 += 1
      print(i + " is " + str(l1) + " levels above than " + input1)
      l2 = parent2.index(i)
      l2 += 1
      print(i + " is " + str(l2) + " levels above than " + input2)
      l3 = parent3.index(i)
      l3 += 1
      print(i + " is " + str(l3) + " levels above than " + input3)
      l4 = parent4.index(i)
      l4 += 1
      print(i + " is " + str(l4) + " levels above than " + input4)
      l5 = parent5.index(i)
      l5 += 1
      print(i + " is " + str(l5) + " levels above than " + input5)
    else:
      print(" No common leader")



# driver code
import json
from functools import reduce

namelist = []
parent1 = []
parent2 = []
parent3 = []
parent4 = []
parent5 = []
parentlist = []
with open('/content/sample_data/org.json') as f:
  data = json.load(f)

answer(data)
