

# edit "subjects" list as necessary, but keep "other" first
subjects = ["other", "latin", "geopolitics", "psychology", "chemistry", "computerprogramming", "philosophy", "precalculus", "debate", "modelun", "boyscouts"]
def rawinput():
    subject = subjectmanager()

def subjectmanager():
    rawsubject = input("subject: ").lower().replace("\\s","")
    print (rawsubject)
rawinput()
    
