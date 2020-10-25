def valid_date(day, mon, year):
  is_valid, is_leap = 1,0
  if (year >= 0 and year <= 9999):
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
      is_leap = 1
    if (mon >= 1 and mon <= 12):
      if (mon == 2):
        if (is_leap and day == 29):
          is_valid = 1
        elif (day > 28):
          is_valid = 0
      elif (mon == 4 or mon == 6 or mon == 9 or mon == 11):
        if (day > 30):
          is_valid = 0
      elif (day > 31):
          is_valid = 0

    else:
      is_valid = 0
  else:
    is_valid = 0

  return is_valid;



def changeformat(s1):
  list1 = s1.split(" ")
  if (len(list1[0])> 3):
    newdate = list1[0][0:2] +'/'
  else:
    newdate = '0'+ list1[0][0:1] +'/'
  month = list1[1][0:3]
  if(month == 'Jan' or month == 'jan'):
    newdate += '01' + '/'
  elif(month == 'feb' or month == 'Feb'):
    newdate += '02' + '/'
  elif(month == 'Mar' or month == 'mar'):
    newdate += '03' + '/'
  elif(month == 'Apr' or month == 'apr'):
    newdate += '04' + '/'
  elif(month == 'may' or month == 'May'):
    newdate += '05' + '/'
  elif(month == 'jun' or month == 'Jun'):
    newdate += '06' + '/'
  elif(month == 'Jul' or month == 'jul'):
    newdate += '07' + '/'
  elif(month == 'aug' or month == 'Aug'):
    newdate += '08' + '/'
  elif(month == 'Sep' or month == 'sep'):
    newdate += '09' + '/'
  elif(month == 'Oct' or month == 'oct'):
    newdate += '10' + '/'
  elif(month == 'Nov' or month == 'nov'):
    newdate += '11' + '/'
  elif(month == 'Dec' or month == 'dec'):
    newdate += '12' + '/'
  newdate += list1[2]
  date2.append(newdate) 

def dateformat(s1):
  d1 = False

  for c in s1:
    if c == '/' or c == '.' or c == '-':
      d1 = True

  if d1:
    date2.append(s1)
  else:
    changeformat(s1)


class Date:  
    def __init__(self, d, m, y):  
        self.d = d          
        self.m = m  
        self.y = y  

monthDays = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]   
def isLeapYear(d):
  return ((d%4 == 0 and d%100 != 0) or d%400 == 0)

def getDifference(dt1, dt2):
  if (dt1.d == dt2.d and dt1.m == dt2.m and dt1.y == dt2.y):
    return 0
  n1 = 0
  if (dt1.y == dt2.y):
    for i in range(dt1.m,dt2.m):
      if (i == 2):
        if (isLeapYear(dt2.y)):
          n1 += 29
        else:
          n1 += 28
      else:
        n1 += monthDays[i]
    n1 -= dt1.d
    n1 += dt2.d
    return n1
  
  n1 = monthDays[dt1.m]
  n1 -= dt1.d
  for i in range(dt1.m+1,13):
    if (i == 2):
      if (isLeapYear(dt1.y)):
        n1 += 29
      else:
        n1 += 28
    else:
      n1 += monthDays[i]
  
  n1 += dt2.d
  for i in range(1,dt2.m):
    if(i == 2):
      if(isLeapYear(dt2.y)):
        n1 += 29
      else:
        n1 += 28
    else:
      n1 += monthDays[i]
  
  if(dt2.y - dt1.y > 1):
    for i in range(dt1.y+1,dt2.y):
      if(isLeapYear(i)):
        n1+= 366
      else:
        n1 += 365
  return n1


def datedifference(dte1,dte2):
  day1,day2 = int(dte1[0:2]),int(dte2[0:2])
  mon1,mon2,year1,year2 = int(dte1[3:5]),int(dte2[3:5]),int(dte1[-4:]),int(dte2[-4:])
  if (valid_date(day1,mon1,year1) == 0 or valid_date(day2,mon2,year2) == 0):
    print("given date is not valid")
  else:
    dt1 = Date(day1,mon1,year1) 
    dt2 = Date(day2,mon2,year2)
    diffd = str(getDifference(dt1, dt2))
    if diffd == '1':
      diff = '1 Day'
    elif diffd == '0':
      diff = '0 Day'
    else:
      diff = diffd + ' Days'
    file_wr = open('/home/dipankar/Desktop/Assignment3/output.txt','a')
    file_wr.write(diff)
    file_wr.write('\n')
    file_wr.close()


file = open('/home/dipankar/Desktop/Assignment3/date_calculator.txt','r')
date1 = []
date2 = []
for l1 in file:
  date1.clear()
  date2.clear()
  l2 = file.readline()
  date1.append(l1.strip())
  date1.append(l2.strip())
  dateformat(date1[0])
  dateformat(date1[1])
  datedifference(date2[0],date2[1])

