from utility import subjectManager
from datetime import datetime
thisweekday = datetime.today().weekday()
thistime = str(datetime.today())
thismonth = int(thistime[5:7])
thisday = int(thistime[8:10])
thisyear = int(thistime[2:4])
leapyears = []
# x in repeatsuntildefault

#Day config
days = ["tomorrow", "today", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
daysindex = [0, 1, 2, 3, 4, 5, 6]
daysdate = [""]
nodaydefaulttotomorrow = False
dayerrordefaulttotomorrow = False


"""
def daysinmonth(month)
if month in [4, 6, 9, 11]:
    return 30
elif thismonth == 2:
    if
    else:
        daysthismonth = 29
else:
    return 31
"""
#Configuration


def newevent():
    rawsubject = input("subject: ")
    newsubject = subjectManager(rawsubject, 0)
    print (newsubject)

"""
    newtitle = input("title: ")
    newday = daymanager(1)
    print (newday)
"""
newevent()
