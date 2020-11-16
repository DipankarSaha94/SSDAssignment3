def addtime(dt1):
  if(dt1.hour>=12):
    if(dt1.minute==0):
      if(dt1.hour>12):
        fhour = int(dt1.hour) - 12
        res = str(fhour)+':'+'00'+'PM'
      else:
        res = str(dt1.hour)+':'+'00'+'PM'
    else:
      if(dt1.hour>12):
        fhour = int(dt1.hour) - 12
        res = str(fhour)+':'+'30'+'PM'
      else:
        res = str(dt1.hour)+':'+'30'+'PM'
  else:
    if(dt1.minute==0):
      res = str(dt1.hour)+':'+'00'+'AM'
    else:
      res = str(dt1.hour)+':'+'30'+'AM'
  return (res)  

def findslot3(dt1,dt2,dt3,dt4,dt5,dt6,h,m):
  dtf = max(dt1,dt3,dt5)
  tdtf = dtf
  dtf = dtf+timedelta(hours=h)+timedelta(minutes=m)
  if (dtf <= min(dt2,dt4,dt6)):
    res1 = addtime(tdtf)
    res2 = addtime(dtf)
    res = res1+' - '+res2
    return res

def findslot4(dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,h,m):
  dtf = max(dt1,dt3,dt5,dt7)
  tdtf = dtf
  dtf = dtf+timedelta(hours=h)+timedelta(minutes=m)
  if (dtf <= min(dt2,dt4,dt6,dt8)):
    res1 = addtime(tdtf)
    res2 = addtime(dtf)
    res = res1+' - '+res2
    return res


def findslot5(dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,dt9,dt10,h,m):
  dtf = max(dt1,dt3,dt5,dt7,dt9)
  tdtf = dtf
  dtf = dtf+timedelta(hours=h)+timedelta(minutes=m)
  if (dtf <= min(dt2,dt4,dt6,dt8,dt10)):
    res1 = addtime(tdtf)
    res2 = addtime(dtf)
    res = res1+' - '+res2
    return res


from datetime import datetime,timedelta
import json

file1 = open('/home/dipankar/Downloads/E1.txt','r')
file2 = open('/home/dipankar/Downloads/E2.txt','r')
file3 = open('/home/dipankar/Downloads/E3.txt','r')
file4 = open('/home/dipankar/Downloads/E4.txt','r')
file5 = open('/home/dipankar/Downloads/E5.txt','r')

str1 = file1.read()
jsonstr = str1.replace('\'','\"')
dict1 = json.loads(jsonstr)

str2 = file2.read()
jsonstr = str2.replace('\'','\"')
dict2 = json.loads(jsonstr)

str3 = file3.read()
jsonstr = str3.replace('\'','\"')
dict3 = json.loads(jsonstr)

str4 = file4.read()
jsonstr = str4.replace('\'','\"')
dict4 = json.loads(jsonstr)

str5 = file5.read()
jsonstr = str5.replace('\'','\"')
dict5 = json.loads(jsonstr)

listo1=[]
listo2=[]
listo3=[]
listo4=[]
listo5=[]

flist1=[]
flist2=[]
flist3=[]
flist4=[]
flist5=[]

a1 = datetime(1900, 1, 1, 9, 0)
a2 = datetime(1900, 1, 1, 17, 0)
n1,n2,n3,n4,n5="","","","",""
givendate1,givendate2,givendate3,givendate4,givendate5 = "","","","",""
inplist = input().split(" ")
noofemp = int(inplist[0])
db = float(inplist[1])
db *= 60
h = int(db/60)
m = int(db%60)

##for 1st employee
for k1,v1 in dict1.items():
  n1 = k1
  for k2,v2 in v1.items():
    givendate1 = k2
    for i in v2:
      s1,s2 = i.split('-')
      listo1.append(datetime.strptime(s1,"%I:%M%p "))
      listo1.append(datetime.strptime(s2," %I:%M%p"))

if(listo1[0]>a1):
  s1,s2 = addtime(a1),addtime(listo1[0])
  s3 = s1+" - "+s2
  flist1.append(s3)
i,l1 = 1,len(listo1)  
while i<(l1 - 1):
  if(listo1[i] != listo1[i+1]):
    flist1.append(addtime(listo1[i])+' - '+addtime(listo1[i+1]))
  i += 2
if(listo1[l1-1]<a2):
  flist1.append(addtime(listo1[l1-1])+' - '+addtime(a2))

## for 2nd eomployee
for k1,v1 in dict2.items():
  n2 = k1
  for k2,v2 in v1.items():
    givendate2 = k2
    for i in v2:
      s1,s2 = i.split('-')
      listo2.append(datetime.strptime(s1,"%I:%M%p "))
      listo2.append(datetime.strptime(s2," %I:%M%p"))


if(listo2[0]>a1):
  flist2.append(addtime(a1)+' - '+addtime(listo2[0]))
i,l2 = 1,len(listo2)  
while i<(l2 - 1):
  if(listo2[i] != listo2[i+1]):
    flist2.append(addtime(listo2[i])+' - '+addtime(listo2[i+1]))
  i += 2
if(listo2[l2-1]<a2):
  flist2.append(addtime(listo2[l2-1])+' - '+addtime(a2))


## for 3nd eomployee
for k1,v1 in dict3.items():
  n3 = k1
  for k2,v2 in v1.items():
    givendate3 = k2
    for i in v2:
      s1,s2 = i.split('-')
      listo3.append(datetime.strptime(s1,"%I:%M%p "))
      listo3.append(datetime.strptime(s2," %I:%M%p"))


if(listo3[0]>a1):
  flist3.append(addtime(a1)+' - '+addtime(listo3[0]))
i,l3 = 1,len(listo3)  
while i<(l3 - 1):
  if(listo3[i] != listo3[i+1]):
    flist3.append(addtime(listo3[i])+' - '+addtime(listo3[i+1]))
  i += 2
if(listo3[l3-1]<a2):
  flist3.append(addtime(listo3[l3-1])+' - '+addtime(a2))


## for 4th eomployee
for k1,v1 in dict4.items():
  n4 = k1
  for k2,v2 in v1.items():
    givendate4 = k2
    for i in v2:
      s1,s2 = i.split('-')
      listo4.append(datetime.strptime(s1,"%I:%M%p "))
      listo4.append(datetime.strptime(s2," %I:%M%p"))


if(listo4[0]>a1):
  flist4.append(addtime(a1)+' - '+addtime(listo4[0]))
i,l4 = 1,len(listo4)  
while i<(l4 - 1):
  if(listo4[i] != listo4[i+1]):
    flist4.append(addtime(listo4[i])+' - '+addtime(listo4[i+1]))
  i += 2
if(listo4[l4-1]<a2):
  flist4.append(addtime(listo4[l4-1])+' - '+addtime(a2))


## for 5th eomployee
for k1,v1 in dict5.items():
  n5 = k1
  for k2,v2 in v1.items():
    givendate5 = k2
    for i in v2:
      s1,s2 = i.split('-')
      listo5.append(datetime.strptime(s1,"%I:%M%p "))
      listo5.append(datetime.strptime(s2," %I:%M%p"))


if(listo5[0]>a1):
  flist5.append(addtime(a1)+' - '+addtime(listo5[0]))
i,l5 = 1,len(listo5)  
while i<(l5 - 1):
  if(listo5[i] != listo5[i+1]):
    flist5.append(addtime(listo5[i])+' - '+addtime(listo5[i+1]))
  i += 2
if(listo5[l5-1]<a2):
  flist5.append(addtime(listo5[l5-1])+' - '+addtime(a2))

listo1.clear()
listo2.clear()
listo3.clear()
listo4.clear()
listo5.clear()

for i in flist1:
  s1,s2 = i.split('-')
  listo1.append(datetime.strptime(s1,"%I:%M%p "))
  listo1.append(datetime.strptime(s2," %I:%M%p"))
for i in flist2:
  s1,s2 = i.split('-')
  listo2.append(datetime.strptime(s1,"%I:%M%p "))
  listo2.append(datetime.strptime(s2," %I:%M%p"))
for i in flist3:
  s1,s2 = i.split('-')
  listo3.append(datetime.strptime(s1,"%I:%M%p "))
  listo3.append(datetime.strptime(s2," %I:%M%p"))
for i in flist4:
  s1,s2 = i.split('-')
  listo4.append(datetime.strptime(s1,"%I:%M%p "))
  listo4.append(datetime.strptime(s2," %I:%M%p"))
for i in flist5:
  s1,s2 = i.split('-')
  listo5.append(datetime.strptime(s1,"%I:%M%p "))
  listo5.append(datetime.strptime(s2," %I:%M%p"))

l1,l2,l3,l4,l5 = len(listo1) - 1,len(listo2) - 1,len(listo3) - 1,len(listo4) - 1,len(listo5) - 1
res3=""

if noofemp == 3:
  for i in range(0,l1,2):
    for j in range(0,l2,2):
      for k in range(0,l3,2):
        res3 = findslot3(listo1[i],listo1[i+1],listo2[j],listo2[j+1],listo3[k],listo3[k+1],h,m)
        if type(res3) == str:
          break
      if type(res3) == str:
        break
    if type(res3) == str:
      break

if noofemp == 4:
  for i in range(0,l1,2):
    for j in range(0,l2,2):
      for k in range(0,l3,2):
        for l in range(0,l4,2):
          res3 = findslot4(listo1[i],listo1[i+1],listo2[j],listo2[j+1],listo3[k],listo3[k+1],listo4[l],listo4[l+1],h,m)
          if type(res3) == str:
            break
        if type(res3) == str:
          break
      if type(res3) == str:
        break
    if type(res3) == str:
      break

if noofemp == 5:
  for i in range(0,l1,2):
    for j in range(0,l2,2):
      for k in range(0,l3,2):
        for l in range(0,l4,2):
          for n in range(0,l5,2):
            res3 = findslot5(listo1[i],listo1[i+1],listo2[j],listo2[j+1],listo3[k],listo3[k+1],listo4[l],listo4[l+1],listo5[n],listo5[n+1],h,m)
            if type(res3) == str:
              break
          if type(res3) == str:
            break
        if type(res3) == str:
          break
      if type(res3) == str:
        break
    if type(res3) == str:
      break

if(type(res3) != str):
  res = "no common slot available "


n1 += ': [\''
file_wr = open('/home/dipankar/Downloads/output.txt','a')
file_wr.write("Available slot")
file_wr.write('\n')
file_wr.write(n1)
l = len(flist1) - 1
for i in range(l):
  file_wr.write(flist1[i])
  file_wr.write("\',\'")

file_wr.write(flist1[l])
file_wr.write("\']")
file_wr.write('\n')
n2 += ': [\''
file_wr.write(n2)
l = len(flist2) - 1
for i in range(l):
  file_wr.write(flist2[i])
  file_wr.write("\',\'")

file_wr.write(flist2[l])
file_wr.write("\']")
file_wr.write('\n')

n3 += ': [\''
file_wr.write(n3)
l = len(flist3) - 1
for i in range(l):
  file_wr.write(flist3[i])
  file_wr.write("\',\'")

file_wr.write(flist3[l])
file_wr.write("\']")
file_wr.write('\n')
if noofemp > 3:
  n4 += ': [\''
  file_wr.write(n4)
  l = len(flist4) - 1
  for i in range(l):
    file_wr.write(flist4[i])
    file_wr.write("\',\'")
  file_wr.write(flist4[l])
  file_wr.write("\']")
  file_wr.write('\n')
  if noofemp == 5:
    n5 += ': [\''
    file_wr.write(n5)
    l = len(flist5) - 1
    for i in range(l):
      file_wr.write(flist5[i])
      file_wr.write("\',\'")
    file_wr.write(flist5[l])
    file_wr.write("\']")
    file_wr.write('\n')

file_wr.write("Slot Duration: ")
db = db/60
file_wr.write(str(db))
file_wr.write('\n')
file_wr.write("{\'")
file_wr.write(givendate1)
file_wr.write("\': [\'")
if res3 is not None: 
  file_wr.write(res3)
else:
  file_wr.write("No common slot is available ")
file_wr.write("\']}")
file_wr.write('\n')
file_wr.close()

