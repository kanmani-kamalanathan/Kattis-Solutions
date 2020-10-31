import calendar 
  
def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
d=input()
date=d+" 2009"
print(findDay(date))
