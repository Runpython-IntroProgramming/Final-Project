import string
import random
from browser.local_storage import storage

#Defining variables
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:;'\"/\\<>(){}[]-=_+?!"
str1 = ""

keylen = ""
keylen += str(random.randint(1, 9))
keylen += str(random.randint(0, 9))
keylen  = int(keylen)

key = ""
key1 = ""
counter = 1
while counter <= keylen:
    key += key1.join(random.choice(associations))
    counter += 1


sitedata = []
running = 0



# Function for encrypting a string
def encrypt(message):
    global associations
    global key
    str1 = ""
    n = 0
    while len(key) < len(message):
        key += key
    associations += associations
    l = len(message)
    while n < l:
        numrepm = associations.find(message[n])
        numrepk = associations.find(key[n])
        finalnum = numrepm + numrepk
        letrep = associations[finalnum]
        str1 = str1 + letrep
        n = n + 1
    return(str1)
  
# Function for decrypting a string  
def decrypt(message):
    global associations
    global key
    str2 = ""
    n = 0
    while len(key) < len(message):
        key += key
    associations += associations
    l = len(message)
    while n < l:
        numrepm1 = associations.find(message[n])
        numrepk1 = associations.find(key[n])
        finalnum1 = numrepm1 - numrepk1
        letrep1 = associations[finalnum1]
        str2 = str2 + letrep1
        n = n + 1
    return(str2)
    
# Function for converting an entered string to a list
def resumelist(code):
    global sitedata
    code1 = code.split()
    lencode = len(code1)
    halflencode = lencode/2
    x = 0
    while x <= halflencode:
        site = code1[0]
        password = code1[1]
        data = []
        data.append(site)
        data.append(password)
        sitedata.append(data)
        del code1[0]
        del code1[0]
        halflencode -= 1
        x += 1

    return(sitedata)
    
def cleardata():
    runcheck = 0
        
        while runcheck == 0:
            
            confirm = input("Are you sure you want to clear local data? Y or N.")
            
            if confirm == "Y":
                try:
                    del storage['key']
                    del storage['pstr']
                    command = input("Cleared. Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords or press q to exit: ")
                    runcheck += 1
                except (KeyError, IndexError, NameError, TypeError):
                    print("No data stored")
                    command = input("Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords or press q to exit: ")
                    runcheck += 1
            elif confirm == "N":
                command = input("Understood. Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords or press q to exit: ")
                runcheck += 1
            else:
                print("Sorry, command not recognized, please try again.")
    
command = input("Welcome! Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords, or press q to exit: ")

try:
    resumecodeentered = storage['pstr']
    sitedata = resumelist(resumecodeentered)
    key = storage['key']
    
except (KeyError, IndexError):
    pass
    
while running == 0:
    

    if command == "s":
        data = []
        site = input("Please enter the name of the site you wish to store: ")
        password = input("Please enter the password belonging to the site: ")
        site = encrypt(site)
        password = encrypt(password)
        data.append(site)
        data.append(password)
        sitedata.append(data)
        code = sitedata.index(data)
        print ("Your site code is: {0}. Please write this down and store it in a safe place so you can access it later.".format(code))
        command = input("Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords, or press q to exit: ")


    elif command == "g":
        code = input("Please enter the code of the site you wish to retrieve: ")
        try:
            code = int(code)
        except ValueError:
            print("Sorry, code not recognized, please try again.")
        code = int(code)
        
        data = sitedata[code]
        site = data[0]
        password = data[1]
        site = decrypt(site)
        password = decrypt(password)
        print("Your password for {0} is {1}.".format(site, password))
        command = input("Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords or press q to exit: ")
        
    elif command == "c":
        cleardata()
        
    elif command == "q":
        printstring = ""
        for p in sitedata:
            printstring = printstring + p[0]
            printstring = printstring + " "
            printstring = printstring + p[1]
            printstring = printstring + " "
        storage['pstr'] = printstring
        storage['key'] = key
        print("Goodbye!")
        running = 1

    else:
        print("Sorry, command not understood. Please try again.")
        command = input("Press s to store a site and password, press g to retrieve a site and password, press c to clear stored passwords or press q to exit: ")
