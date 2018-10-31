#repeatsUntilDefault = 2
#SUBJECTMANAGER
#configuration
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
    #edit "subjects" list as necessary, but keep "other" first
noSubjectDefaultOther = True
#subjectErrorDefaultOther = False

def subjectManager(rawsubject, repeat):
    rawsubject = rawsubject.lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            if noSubjectDefaultOther:
                return s
            elif len(rawsubject) > 0:
                return s
#    print ("Does not match a subject.")
        elif subjectErrorDefaultOther:
# or repeat >= repeatsUntilDefault
#           print ('Defaulting to "other".')
            return "other"
"""
    else:
        repeat += 1
        subject2 = subjectManager(repeat)
        return subject2
"""
