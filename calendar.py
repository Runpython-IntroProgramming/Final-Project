

# edit "subjects" list as necessary, but keep "other" first
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
def rawinput():
    subject = subjectmanager()
    print (subject)
def subjectmanager():
    rawsubject = input("subject: ").lower().replace(" ","")
    for s in subjects:
        if rawsubject == s[0:len(rawsubject)]:
            return s
    print ("Does not match a subject. Try again")
    subjectmanager()
rawinput()
    
