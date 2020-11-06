def addtime(dt1,dt2):
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
  
  if(dt2.hour>=12):
    if(dt2.minute==0):
      if(dt2.hour>12):
        fhour2 = int(dt2.hour) - 12
        res2 = str(fhour2)+':'+'00'+'PM'
      else:
        res2 = str(dt2.hour)+':'+'00'+'PM'
    else:
      if(dt2.hour>12):
        fhour2 = int(dt2.hour) - 12
        res2 = str(fhour2)+':'+'30'+'PM'
      else:
        res2 = str(dt2.hour)+':'+'30'+'PM'
  else:
    if(dt2.minute==0):
      res2 = str(dt2.hour)+':'+'00'+'AM'
    else:
      res2 = str(dt2.hour)+':'+'30'+'AM'
  
  return (res+' - '+res2)


def findslot(dt1,dt2,dt3,dt4,h,m):
  if (dt1 >= dt3):
    dt5 = dt1+timedelta(hours=h)
    dt5 = dt5+timedelta(minutes=m)
    if (dt5 <= dt2 and dt5 <= dt4):
      res = addtime(dt1,dt5)
      return res
  else:
    dt5 = dt3+timedelta(hours=h)
    dt5 = dt5+timedelta(minutes=m)
    if (dt5 <= dt2 and dt5 <= dt4):
      res = addtime(dt3,dt5)
      return res



#driver code

from datetime import datetime,timedelta
import json

file1 = open('/home/dipankar/Desktop/Assignment3/Employee1.txt','r')
file2 = open('/home/dipankar/Desktop/Assignment3/Employee2.txt','r')
str1 = file1.read()
jsonstr = str1.replace('\'','\"')
dict1 = json.loads(jsonstr)
str2 = file2.read()
jsonstr2 = str2.replace('\'','\"')
dict2 = json.loads(jsonstr2)
listo1=[]
listo2=[]
flist1=[]
flist2=[]
a1 = datetime(1900, 1, 1, 9, 0)
a2 = datetime(1900, 1, 1, 17, 0)
n1,n2="",""
givendate1,givendate = "",""
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
  flist1.append(addtime(a1,listo1[0]))
i,l1 = 1,len(listo1)  
while i<(l1 - 1):
  if(listo1[i] != listo1[i+1]):
    flist1.append(addtime(listo1[i],listo1[i+1]))
  i += 2
if(listo1[l1-1]<a2):
  flist1.append(addtime(listo1[l1-1],a2))

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
  flist2.append(addtime(a1,listo2[0]))
i,l2 = 1,len(listo2)  
while i<(l2 - 1):
  if(listo2[i] != listo2[i+1]):
    flist2.append(addtime(listo2[i],listo2[i+1]))
  i += 2
if(listo2[l2-1]<a2):
  flist2.append(addtime(listo2[l2-1],a2))

listo2.clear()
listo1.clear()
for i in flist1:
  s1,s2 = i.split('-')
  listo1.append(datetime.strptime(s1,"%I:%M%p "))
  listo1.append(datetime.strptime(s2," %I:%M%p"))


for i in flist2:
  s1,s2 = i.split('-')
  listo2.append(datetime.strptime(s1,"%I:%M%p "))
  listo2.append(datetime.strptime(s2," %I:%M%p"))

l1,l2 = len(listo1) - 1,len(listo2) -1
db = float(input())
db *= 60
h = int(db/60)
m = int(db%60)
res3=""
for i in range(0,l1,2):
  for j in range(0,l2,2):
    res3 = findslot(listo1[i],listo1[i+1],listo2[j],listo2[j+1],h,m)
    if type(res3) == str:
      break
  if type(res3) == str:
    break

n1 += ': [\''
file_wr = open('/home/dipankar/Desktop/Assignment3/output.txt','a')
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
file_wr.write("Slot Duration: ")
db = db/60
file_wr.write(str(db)+ " Hour")
file_wr.write('\n')
file_wr.write("{\'")
file_wr.write(givendate1)
file_wr.write("\': [\'")
if res3 is not None:
  file_wr.write(res3)
else:
  file_wr.write("No common slot is available ")
file_wr.write("\']}")
file_wr.close()
