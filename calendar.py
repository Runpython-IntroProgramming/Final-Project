

# edit "subjects" list as necessary, but keep "other" first
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]

subjectdefaultother = False


def rawinput():
    subject = subjectmanager()
    print (subject)

def subjectmanager():
    rawsubject = input("subject: ").lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            return s
    if
    if subjectdefaultother:
        print ('Does not match a subject. Defaulting to "other".')
        return "other"
    
rawinput()
    