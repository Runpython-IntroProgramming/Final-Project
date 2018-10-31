#SUBJECTMANAGER
#configuration
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
    #edit "subjects" list as necessary, but keep "other" first
nosubjectdefaulttoother = False
subjecterrordefaulttoother = False

def subjectManager(rawsubject, repeat):
    rawsubject = rawsubject.lower().replace(" ","")
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
