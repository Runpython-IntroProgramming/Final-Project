

# edit "subjects" list as necessary, but keep "other" first
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]

subjectdefaultother = False


def rawinput():
    subject = subjectmanager(1)
    print (subject)

def subjectmanager(repeat):
    rawsubject = input("subject: ").lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            return s
    print ("Does not match a subject.")
    if subjectdefaultother or repeat > 2:
        print ('Defaulting to "other".')
        return "other"
    repeat += 1
    subject2 = subjectmanager(repeat)
    return subject2
        
    
rawinput()
    