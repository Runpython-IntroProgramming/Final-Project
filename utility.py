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
###subjectManager###

###dateManager###
daysoftheweek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def dateManager(rawdate):
    rawdate = rawdate.lower().replace("-","/").replace("~","/")
    skip = 0
    if rawdate[0:5] == "next ":
        skip = 5
    for day in daysoftheweek:
        if rawdate[skip:len(rawdate)] == day[0:len(rawsubject) - skip]:
            return l
dateManager("next mon")
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
import datetime
import calendar
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