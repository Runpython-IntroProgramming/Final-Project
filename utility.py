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
thisyear = datetime.now().year
today = datetime.now().date()
def wordToDate(day, skip):
    days = []
    if day == "today":
        return today
    elif day == "tomorrow":
        return today + timedelta(days=1)
    else:
        for x in range(7):
            if day == (today + timedelta(days=x)).weekday():
                if skip == 5:
                    return today + timedelta(days=x+7)
                else:
                    return today + timedelta(days=x)

daywords = ["tomorrow", "today", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def dateManager(rawdate):
    rawdate = rawdate.lower().replace("-","/").replace("~","/")
    skip = 0
    if rawdate[0:5] == "next ":
        skip = 5
    for day in daywords:
        if rawdate[skip:len(rawdate)] == day[0:len(rawdate) - skip]:
            return wordToDate(daywords.index(day)-2, skip)
    
    slashlist = []
    for index in range(len(rawdate)):
        if rawdate[index] == "/":
            slashlist.append(index)
    toslash1 = rawdate[0:slashlist[0]]
    month = int(toslash1)
    if month in range(1,13):
        if len(slashlist) == 1:
            slash1toend = rawdate[slashlist[0]+1:len(rawdate)]
            year = thisyear
            day = int(slash1toend)
        elif len(slashlist) == 2:
            slash2toend = rawdate[slashlist[1]+1:len(rawdate)]
            slash1toslash2 = rawdate[slashlist[0]+1:slashlist[1]]
            if len(slash2toend) == 0:
                year = thisyear
            elif len(slash2toend) in range(1,4):
                year = int(slash2toend) + int(str(thisyear)[0])*1000
            elif len(slash2toend) == 4:
                year = int(slash2toend)
            day = int(slash1toslash2)
        if day in range(1,monthrange(year,month)[1]+1):
            return datetime(year, month, day).date()
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