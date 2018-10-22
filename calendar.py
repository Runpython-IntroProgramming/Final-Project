

# edit "subjects" list as necessary, but keep "other" first
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]

subjectdefaultother = True


def rawinput():
    subject = subjectmanager()
    print (subject)
def subjectmanager():
    rawsubject = input("subject: ").lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            return s

    if subjectdefaultother:
        print ('Does not match a subject. Default to "other".')
        return "other"
rawinput()
    
