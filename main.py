from utility import subjectManager
# x in repeatsuntildefault

#Day config
days = ["tomorrow", "today", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
daysindex = [0, 1, 2, 3, 4, 5, 6]
daysdate = [""]
nodaydefaulttotomorrow = False
dayerrordefaulttotomorrow = False




def newevent():
    rawsubject = input("subject: ")
    newsubject = subjectManager(rawsubject)
    print (newsubject)
    


newevent()
