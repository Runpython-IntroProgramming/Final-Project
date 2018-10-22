from datetime import datetime

#Configuration
repeatsuntildefault = 2

#Subject config
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
# edit "subjects" list as necessary, but keep "other" first
nosubjectdefaulttoother = False
subjecterrordefaulttoother = False

#Day config
days = ["tomorrow", "today", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
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
    if month 1:12 day 1:31 year
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
    for d in days:
        if rawday == s[0:len(rawday)]:
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
        
newevent()
print (datetime.today())
    