from datetime import datetime
thisweekday = datetime.today().weekday()
thistime = str(datetime.today())
thismonth = int(thistime[5:7])
thisday = int(thistime[8:10])
thisyear = int(thistime[2:4])
leapyears = []
for x in repeatsuntildefault

def daysinmonth(month)
if month in [4, 6, 9, 11]:
    return 30
elif thismonth == 2:
    if
    else:
        daysthismonth = 29
else:
    return 31
#Configuration
repeatsuntildefault = 2

#Subject config
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
# edit "subjects" list as necessary, but keep "other" first
nosubjectdefaulttoother = False
subjecterrordefaulttoother = False

#Day config
days = ["tomorrow", "today", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
daysindex = [0, 1, 2, 3, 4, 5, 6]
daysdate = [""]
nodaydefaulttotomorrow = False
dayerrordefaulttotomorrow = False

def newevent():
    newsubject = subjectmanager(1)
    print (newsubject)
    newtitle = input("title: ")
    newday = daymanager(1)
    print (newday)

def subjectmanager(repeat):
    rawsubject = input("subject: ").lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            if nosubjectdefaulttoother:
                return s
            elif len(rawsubject) > 0:
                return s
    print ("Does not match a subject.")
    if subjecterrordefaulttoother or repeat > repeatsuntildefault:
        print ('Defaulting to "other".')
        return "other"
    else:
        repeat += 1
        subject2 = subjectmanager(repeat)
        return subject2
        
def daymanager(repeat):
    rawday = input("day: ").lower().replace(" ","-").replace("/","-")
#    if rawday > 0 and rawday < 32:
        
    for d in days:
        if rawday == d[0:len(rawday)]:
            if nodaydefaulttotomorrow:
                return d
            elif len(rawday) > 0:
                return d
    print ("Does not match a day.")
    if dayerrordefaulttotomorrow or repeat > repeatsuntildefault:
        print ('Defaulting to "tomorrow".')
        return "tomorrow"
    else:
        repeat += 1
        day2 = daymanager(repeat)
        return day2
        
#newevent()
    
