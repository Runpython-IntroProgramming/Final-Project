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

###calendarManager###
import datetime
import calendar
"""
def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
def daysInMonth(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif thismonth == 2:
        if leapYear(year):
            return 29
        else:
            return 28
    else:
        return 31
"""

def calendarManager(month, year):
    for day in range(1,calendar.monthrange(year, month)[1]+1):
        days.append(day)


print(datetime.datetime(2018, 10, 31, 13))
print(datetime.datetime.today().weekday())
