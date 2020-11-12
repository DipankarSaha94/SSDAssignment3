def changeformat(s1):
  list1 = s1.split(" ")
  if (len(list1[0])> 3):
    newdate = list1[0][0:2] +'/'
  else:
    newdate = '0'+ list1[0][0:1] +'/'
  month = list1[1][0:3]
  for i in range(10):
  	if month == months[i]:
  		newdate += '0' + str(i) + '/'
  for i in range(10,13):
  	if month == months[i]:
  		newdate += str(i) + '/'  
  newdate += list1[2]
  return newdate

class Date:  
    def __init__(self, d, m, y):  
        self.d = d          
        self.m = m  
        self.y = y  

monthDays = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]   
months = ['0', 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def isLeapYear(d):
  return ((d%4 == 0 and d%100 != 0) or d%400 == 0)

def noofdays(m1,m2,y):
  n = 0
  for i in range(m1,m2):
    if (i == 2):
      if (isLeapYear(y)):
        n += 29
      else:
        n += 28
    else:
      n += monthDays[i]
  return n

def getDifference(dt1, dt2):
  if (dt1.d == dt2.d and dt1.m == dt2.m and dt1.y == dt2.y):
    return 0
  n1 = 0
  if (dt1.y == dt2.y):
    n1 = noofdays(dt1.m,dt2.m,dt2.y)
    n1 -= dt1.d
    n1 += dt2.d
    return n1
  
  n1 = noofdays(dt1.m,dt1.m+1,dt1.y)
  n1 -= dt1.d
  n1 += noofdays(dt1.m+1,13,dt1.y)
  n1 += dt2.d
  n1 += noofdays(1,dt2.m,dt2.y)
  
  if(dt2.y - dt1.y > 1):
    for i in range(dt1.y+1,dt2.y):
      if(isLeapYear(i)):
        n1+= 366
      else:
        n1 += 365
  return n1


def datedifference(dte1,dte2):
  day1,day2 = int(dte1[dpos:dpos+2]),int(dte2[dpos:dpos+2])
  mon1,mon2,year1,year2 = int(dte1[mpos:mpos+2]),int(dte2[mpos:mpos+2]),int(dte1[ypos:ypos+4]),int(dte2[ypos:ypos+4])
  dt1 = Date(day1,mon1,year1) 
  dt2 = Date(day2,mon2,year2)
  diffd = str(getDifference(dt1, dt2))
  if diffd == '1':
    diff = '1 Day'
  elif diffd == '0':
    diff = '0 Day'
  else:
    diff = diffd + ' Days'
  file_wr = open('/home/dipankar/Downloads/output.txt','a')
  file_wr.write(diff)
  file_wr.write('\n')
  file_wr.close()


import sys
file = open('/home/dipankar/Downloads/date_calculator.txt','r')
date1 = []
dtype = False
dpos,mpos,ypos = 0,0,0
try:
  formatstring = sys.argv[1]
  formatstring = formatstring.strip()
  if len(formatstring) > 9:
    for i in range(len(formatstring)):
      if formatstring[i] == 'd':
        dpos = i
      elif formatstring[i] == 'm':
        mpos = i
      elif formatstring[i] == 'y':
        ypos = i
    dpos,mpos,ypos = dpos-1,mpos-1,ypos-3
except IndexError:
  dtype =True

for l1 in file:
  date1.clear()
  l2 = file.readline()
  date1.append(l1.strip())
  date1.append(l2.strip())
  if dtype == True:
    date1[0] = changeformat(date1[0])
    date1[1] = changeformat(date1[1])
    dpos,mpos,ypos = 0,3,6
    datedifference(date1[0],date1[1])
  else:
    datedifference(date1[0],date1[1])

