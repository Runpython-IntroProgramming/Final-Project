###subjectManager###
#configuration
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
    #edit "subjects" list as necessary, but keep "other" first
noSubjectDefaultOther = True
subjectErrorDefaultOther = True
def subjectManager(rawsubject):
    rawsubject = rawsubject.lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            if noSubjectDefaultOther:
                return s
            elif len(rawsubject) > 0:
                return s
        elif subjectErrorDefaultOther:
            return "other"

###dateManager###
from datetime import datetime, timedelta
from calendar import calendar, monthrange
def wordToDate(day, skip):
    days = []
    if day == "today":
        return datetime.now().date()
    elif day == "tomorrow":
        return datetime.now().date() + timedelta(days=1)
    else:
        for x in range(7):
            if day == (datetime.now().date() + timedelta(days=x)).weekday():
                if skip == 5:
                    return datetime.now().date() + timedelta(days=x+7)
                else:
                    return datetime.now().date() + timedelta(days=x)

daywords = ["tomorrow", "today", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def dateManager(rawdate):
    rawdate = rawdate.lower().replace("-","/").replace("~","/")
    skip = 0
    if rawdate[0:5] == "next ":
        skip = 5
    for day in daywords:
        if rawdate[skip:len(rawdate)] == day[0:len(rawdate) - skip]:
            return wordToDate(daywords.index(day)-2, skip)
    if int(rawdate[0:2]) in range(1,13) and rawdate[2] == "/":
        month = int(rawdate[0:2])
        if rawdate[5] == "/":
            if type(int(rawdate[6:10])) == int and type(int(rawdate[8:10])) == int:
                year = int(rawdate[6:10])
            elif type(int(rawdate[6:8])) == int:
                year = int(rawdate[6:8]) + 2000
            else:
                year = datetime.now().year
        else:
            year = datetime.now().year
        if int(rawdate[3:5]) in range(1,monthrange(year,month)[1]+1):
            day = int(rawdate[3:5])
            return datetime(year, month, day).date()
        else:
            return
    else:
        return
print(dateManager(input("Write a day of the week or date in (mm/dd/yyyy). DateManager will retrieve the numerical date: ")))
"""
            if noSubjectDefaultOther:
                return l
            elif len(rawsubject) > 0:
                return s
        elif subjectErrorDefaultOther:
            return "other"
"""
"""
###calendarManager###

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, KeyEvent, MouseEvent
black = Color(0x000000, 1.0)
grey = Color(0x808080, 1.0)
white = Color(0xffffff, 1.0)
line = LineStyle(1, black)

deadcell = RectangleAsset(10, 10, line, black)

newcell = RectangleAsset(10, 10, line, white)

oldcell = RectangleAsset(10, 10, line, grey)

def calendarManager(year, month):
    for day in range(1,calendar.monthrange(year, month)[1]+1):
        Sprite(datetime.datetime(year, month, day).weekday()


print(datetime.datetime(2018, 10, 31, 13))
print(datetime.datetime.today().weekday())

calendarManager(2018,10)

app = App()
app.run()
"""