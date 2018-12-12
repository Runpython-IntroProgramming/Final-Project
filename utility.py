from datetime import datetime, timedelta
from calendar import calendar, monthrange
thisyear = datetime.now().year
today = datetime.now().date
with open("subjectDump.txt", 'r') as d:
    subjects = [line.rstrip('\n') for line in d]

def saveSubjects():
    with open('subjectDump.txt', 'w') as d:
        for s in subjects:
            d.write(str(s) + '\n')

def addSubject(subject):
    subject = str(subject)
    reserved = ["today", "tomorrow", "next", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    conflict = False
    for r in reserved:
        if subject == r[:len(subject)]:
            conflict = True
    for s in subjects:
        if subject == s[:len(subject)]:
            conflict = True
    if not conflict:
        subjects.append(subject)
    saveSubjects()

def delSubject(subject):
    if subject in subjects:
        subjects.remove(subject)
    saveSubjects()

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
def weekdayManager(rawInput):
    for d in days:
        if rawInput == d[:len(rawInput)]:
            return days.index(d),rawInput[len(d)+1:]







def orderManager(rawInput):
#tests 11th - 13th
    if rawInput[:4] == "11th":
        return 11, rawInput[5:]
    elif rawInput[:4] == "12th":
        return 12, rawInput[5:]
    elif rawInput[:4] == "13th":
        return 13, rawInput[5:]
#tests 1st -10th 14th - 366th
    for num in list(range(1,11)) + list(range(14,367)):
        if str(num)[-1] == "1":
            th = str(num) + "st"
        elif str(num)[-1] == "2":
            th = str(num) + "nd"
        elif str(num)[-1] == "3":
            th = str(num) + "rd"
        else:
            th = str(num) + "th"
        if rawInput[:len(th)] == th:
            return num, rawInput[len(th)+1:]
#tests 1 - 366
    a = [0]
    for n in range(1,367):
        if rawInput[:len(str(n))] == str(n):
            a.append(n)
    if len(a) > 1:
        return a[-1],rawInput[len(str(a[-1]))+1:]
#tests first - threehundredninetyninth
    teens = ["eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "ninteenth"]
    ieths = ["tenth", "twentieth", "thirtieth", "fortieth", "fiftieth", "sixtieth", "seventieth", "eightieth", "nintieth"]
    hundreths = ["one hundreth", "two hundreth", "three hundreth"]
    ones = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"]
    tens = ["twenty-", "thirty-", "forty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"]
    hundreds = ["", "one hundred ", "two hundred ", "three hundred "]
    for hundred in hundreds:
        for teen in teens:
            num = hundred + teen
            if num == rawInput[0:len(num)]:
                return hundreds.index(hundred) * 100 + teens.index(teen) + 11, rawInput[len(num)+1:]
        for ieth in ieths:
            num = hundred + ieth
            if num == rawInput[0:len(num)]:
                return hundreds.index(hundred) * 100 + (ieths.index(ieth) + 1) * 10, rawInput[len(num)+1:]
        for ten in tens:
            for one in ones:
                num = hundred + ten + one
                if num == rawInput[0:len(num)]:
                    return hundreds.index(hundred) * 100 + (tens.index(ten) + 2) * 10 + ones.index(one) + 1, rawInput[len(num)+1:]
    for hundreth in hundreths:
        if hundreth == rawInput[0:len(hundreth)]:
            return (hundreths.index(hundreth) + 1) * 100, rawInput[len(hundreth)+1:]
    for one in ones:
        if one == rawInput[0:len(one)]:
            return ones.index(one) + 1, rawInput[len(one)+1:]

def numericalDateManager(rawInput):
    rawdate = rawInput.replace("-","/").replace("~","/")
    slashlist = []
    for index in range(len(rawdate)):
        if rawdate[index] == "/":
            slashlist.append(index)
    toslash1 = rawdate[0:slashlist[0]]
    month = int(toslash1)
    if month in range(1,13):
        if len(slashlist) == 1:
            slash1toend = rawdate[slashlist[0]+1:]
            year = thisyear
            day = int(slash1toend)
        elif len(slashlist) == 2:
            slash2toend = rawdate[slashlist[1]+1:]
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

def dynamicDateManager(rawInput):
    print("test")

def staticDateManager(rawInput, modifier):
    if rawInput == "tomorrow"[0:len(rawInput)]:
        return today() + timedelta(days=1)
    if rawInput == "today"[0:len(rawInput)]:
        return today()
#finds "next mon" and "mon"
    try:
        for x in range(7):
            if weekdayManager(rawInput)[0] == (today() + timedelta(days=x)).weekday():
                if 0 in modifier:
                    return today() + timedelta(days=x+7)
                else:
                    return today() + timedelta(days=x)
    except:
        try:
            numericalDate = numericalDateManager(rawInput)
            return numericalDate
            order,rawInput = orderManager(rawInput)
            print (order)
            print (rawInput)
            """
            interval = weekdayManager(rawInput)[0]
            rawInput = weekdayManager(rawInput)[1]
            print (interval)
            print(rawInput)
            """
        except:
            """
            interval = monthManager(rawInput)[0]
            """
#finds "3rd mon of october" or "5th mon" or "5th mon"






    """
    return numericalDateManager(rawInput)
    """
def tagManager(rawInput):
    rawInput = rawInput.lower()

    rawSubject = rawInput.replace(" ","")
    for s in subjects:
        if rawSubject == s[0:len(rawSubject)]:
            return s

    rawInput = rawInput.replace("the ", "").replace("in ","").replace("of ", "")
    modifiers = ["next ", "until ", "every "]
    modifier = []
    for m in modifiers:
        if rawInput[0:len(m)] == m:
            modifier.append(modifiers.index(m))
            rawInput = rawInput[len(m):len(rawInput)]
    for m in modifiers:
        if rawInput[0:len(m)] == m:
            modifier.append(modifiers.index(m))
            rawInput = rawInput[len(m):len(rawInput)]

    if 2 in modifier:
        return dynamicDateManager(rawInput)
    else:
        return staticDateManager(rawInput, modifier)





"""
    if modifier == 0

    else:





    if modifier == 1:
        orders = ["1st", "first", "2nd", "second", "3rd", "third", "4th", "fourth", "5th", "fifth"]
        for o in orders


class Recurr():
    def __init__(self, interval, end)
class WeekdayRecurr():
    def __init__(self, interval, end)
class Recurr():
    def __init__(self, interval, end)
class Event():
    def __init__(self, name, body, tags):
        self.name() = name
        self

"""



run = True
while run:
    choice = input("Type 'i' for an input, 'a' to add a subject, or 'd' to delete a subject. Type 'e' to exit.")
    if choice == "i":
        print(tagManager(input("Write Something: ")))
    elif choice == "a":
        print (subjects)
        addSubject(input("type what you want to add"))
        print (subjects)
    elif choice == "d":
        print (subjects)
        delSubject(input("type what you want to delete"))
        print (subjects)
    elif choice == "e":
        run = False
