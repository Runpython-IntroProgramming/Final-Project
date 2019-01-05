import pygame
import datetime
import utility

def get_weekday(key_day):
    key_weekday = key_day.weekday() + 1
    if key_weekday == 7:
        key_weekday = 0
    return key_weekday


def get_week(key_day):
    key_week = []
    key_weekday = get_weekday(key_day)
    for i in range(0, key_weekday):
        key_week.insert(0, key_day - datetime.timedelta(days=i + 1))
    key_week.append(key_day)
    for i in range(key_weekday + 1, 7):
        key_week.append(key_day - datetime.timedelta(days=key_weekday - i))

    return key_week


def get_weeks(key_day):
    last_week = get_week(key_day - datetime.timedelta(days=7))
    this_week = get_week(key_day)
    next_week = get_week(key_day + datetime.timedelta(days=7))
    week_after = get_week(key_day + datetime.timedelta(days=14))
    key_weeks = [last_week, this_week, next_week, week_after]
    return key_weeks


today = datetime.datetime.today().date()
weekday = get_weekday(today)
weekdayWords = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekdayWord = weekdayWords[weekday]
thisMonth = today.month
thisDay = today.day
thisYear = today.year
weeks = get_weeks(today)
width = 400
height = 650

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calendar")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
color = (255, 255, 255)
specialColor = (250, 250, 0)
font = "Courier New"
font20 = pygame.font.SysFont(font, 20)
font10 = pygame.font.SysFont(font, 10)

calendarWidth = width - 50
calendarHeight = height/2 - 50
calendar = pygame.Surface((calendarWidth, calendarHeight), pygame.SRCALPHA, 32)

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
shiftNumbers = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

otherKeys = ['`', '-', '=', '[', ']', '\\', ';', '\'', ',', '.', '/']
shiftOtherKeys = ['~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']

for x in range(1, 7):
    pygame.draw.line(calendar, color, (x * calendarWidth / 7, 0), (x * calendarWidth / 7, calendarHeight))
for y in range(1, 4):
    pygame.draw.line(calendar, color, (0, y * calendarHeight / 4), (calendarWidth, y * calendarHeight / 4))
for w in range(4):
    for d in range(7):
        if weeks[w][d] == today:
            num = font10.render(str(weeks[w][d].day), False, specialColor)
        else:
            num = font10.render(str(weeks[w][d].day), False, color)
        calendar.blit(num, (calendarWidth / 7 * d + 1, calendarHeight / 4 * w + 1))

textBox = pygame.Surface((width-50, 50), pygame.SRCALPHA, 32)
pygame.draw.line(textBox, color, (0, 50), (width, 50), 3)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


backgrounds = ["obunga", "chungus", "field", "camp", "garden"]
backgroundIndex = 3


def cycle_background(index):
    if index == len(backgrounds) - 1:
        index = 0
    else:
        index += 1
    return index



run = True
update = True
rawInput = ""
subjectInput = ""
timeInput = ""
subjectOutput = ""
timeOutput = ""
subjectOutputCheck = ""
timeOutputCheck = ""
screen = 2
box = 0
selectedDay = today
while run:
    if update:
        pygame.display.update()
    background = Background(backgrounds[backgroundIndex] + ".png", [0, 0])
    window.blit(background.image, background.rect)
    if screen == 1:
        pygame.draw.polygon(window, color, ((width - 50, 25), (width - 25, 25), (width - 25, 50), (width - 50, 50)), 1)
        subjectTitle = font20.render("Enter a date", False, color)
        subjectTitleCoord = subjectTitle.get_rect(center=(width / 2, height/2 - 100))
        window.blit(textBox, (25, height / 2 - 90))
        window.blit(subjectTitle, subjectTitleCoord)
        words = font20.render("{0}".format(timeInput), False, color)
        window.blit(words, (25, height / 2 - 65))

        dateTitle = font20.render("Enter a subject", False, color)
        dateTitleCoord = dateTitle.get_rect(center=(width / 2, height/2 - 200))
        window.blit(textBox, (25, height / 2 - 190))
        window.blit(dateTitle, dateTitleCoord)
        words = font20.render("{0}".format(subjectInput), False, color)
        window.blit(words, (25, height / 2 - 165))

        title = font20.render("Name your event", False, color)
        titleCoord = title.get_rect(center=(width / 2, height / 2))
        window.blit(title, titleCoord)
        window.blit(textBox, (25, height / 2 + 10))
        words = font20.render("{0}".format(rawInput), False, color)
        window.blit(words, (25, height / 2 + 35))

    elif screen == 2:
        pygame.draw.polygon(window, color, ((width - 50, 25), (width - 25, 25), (width - 25, 50), (width - 50, 50)), 1)
        pygame.draw.polygon(window, color, ((50, 25), (25, 25), (25, 50), (50, 50)), 1)
        window.blit(calendar, (25, height / 2 + 25))
        title = font20.render("{0} {1}-{2}-{3}".format(weekdayWords[get_weekday(selectedDay)], selectedDay.month, selectedDay.day, str(selectedDay.year)[-2:]), False, color)
        titleCoord = title.get_rect(center=(width / 2, height / 2))
        window.blit(title, titleCoord)
        events = utility.getEvents()
        tasks = []
        for e in events:

            if not str(e[0] - selectedDay)[0] == "-":
                tasks.append(e)
        for t in tasks:
            task = font10.render("{0}: {1} due {2}, {3}".format(t[1], t[2], weekdayWords[get_weekday(t[0])], t[0]), False, color)
            taskCoord = task.get_rect(center=(width / 2, 15 * tasks.index(t) + 100))
            window.blit(task, taskCoord)

    elif screen == 3:
        pygame.draw.polygon(window, color, ((50, 25), (25, 25), (25, 50), (50, 50)), 1)
        window.blit(textBox, (25, height / 2 + 25))
        title = font20.render("Enter a subject", False, color)
        titleCoord = title.get_rect(center=(width / 2, height / 2))
        window.blit(title, titleCoord)
        words = font20.render("{0}".format(rawInput), False, color)
        window.blit(words, (35, height/2 + 50))
        pygame.draw.polygon(window, color, ((width/2 - 100, height / 2 + 150), (width/2 - 50, height / 2 + 150)), 1)
        pygame.draw.polygon(window, color, ((width / 2 + 100, height / 2 + 150), (width / 2 + 50, height / 2 + 150), (width / 2 + 75, height / 2 + 150), (width / 2 + 75, height / 2 + 175), (width / 2 + 75, height / 2 + 125), (width / 2 + 75, height / 2 + 150)), 1)
        with open("subjectDump.txt", 'r') as d:
            subjects = [line.rstrip('\n') for line in d]

        for s in subjects:
            subjectLine = font10.render(s, False, color)
            subjectLineCoord = subjectLine.get_rect(center=(width/2 - 75, 10 * subjects.index(s) + 100))
            window.blit(subjectLine, subjectLineCoord)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if screen == 1:
                if box == 1:
                    if event.key == pygame.K_BACKSPACE:
                        subjectInput = subjectInput[0:-1]
                    elif event.key == pygame.K_RETURN:
                        subjectOutput = utility.subjecttagmanager(subjectInput)
                        subjectInput = subjectOutput
                        subjectOutputCheck = True
                    for l in letters + numbers:
                        if str(chr(event.key)) == l:
                            subjectInput += chr(event.key)

                elif box == 2:
                    if event.key == pygame.K_BACKSPACE:
                        timeInput = timeInput[0:-1]
                    elif event.key == pygame.K_SPACE:
                        timeInput += " "
                    elif event.key == pygame.K_RETURN:
                        timeOutput = utility.datetagmanager(timeInput)
                        timeInput = str(timeOutput)
                        timeOutputCheck = True
                    else:
                        for k in letters + numbers + otherKeys:
                            if str(chr(event.key)) == k:
                                timeInput += chr(event.key)
                elif box == 3:
                    if event.key == pygame.K_BACKSPACE:
                        rawInput = rawInput[0:-1]
                    elif event.key == pygame.K_SPACE:
                        rawInput += " "
                    elif event.key == pygame.K_RETURN:
                        if subjectOutputCheck and timeOutputCheck:
                            utility.addEvent(timeOutput, subjectOutput, rawInput)
                    else:
                        for k in letters + numbers + otherKeys:
                            if str(chr(event.key)) == k:
                                rawInput += chr(event.key)
            elif screen == 2:
                if event.key == pygame.K_f:
                    backgroundIndex = cycle_background(backgroundIndex)
            elif screen == 3 and box == 4:
                if event.key == pygame.K_BACKSPACE:
                    rawInput = rawInput[0:-1]
                for l in letters + numbers:
                    if str(chr(event.key)) == l:
                        rawInput += chr(event.key)

            pygame.display.update()

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            if 25 < mouse[0] < width - 25:
                if screen == 1:
                    if height / 2 - 200 < mouse[1] < height / 2 - 100:
                        box = 1
                    elif height / 2 - 100 < mouse[1] < height / 2:
                        box = 2
                    elif height / 2 < mouse[1] < height / 2 + 80:
                        box = 3
                    else:
                        box = 0

                if screen == 2:
                    if height / 2 + 25 < mouse[1] < height - 25:
                        calendarMouse = (mouse[0] - 25, mouse[1] - (height / 2 + 25))
                        for x in range(7):
                            if calendarWidth / 7 * x < calendarMouse[0] < calendarWidth / 7 * (x + 1):
                                for y in range(4):
                                    if calendarHeight / 4 * y < calendarMouse[1] < calendarHeight / 4 * (y + 1):
                                        print(weeks[y][x])
                                        selectedDay = weeks[y][x]
                                        update = True
                if screen == 3:
                    if height / 2 + 25 < mouse[1] < height / 2 + 75:
                        box = 4
                    elif height / 2 + 125 < mouse[1] < height / 2 + 175:
                        if width/2 - 100 < mouse[0] < width/2 - 50:
                            utility.delSubject(rawInput)
                            with open("subjectDump.txt", 'r') as d:
                                subjects = [line.rstrip('\n') for line in d]
                        elif width / 2 + 50 < mouse[0] < width / 2 + 100:
                            utility.addSubject(rawInput)
                            with open("subjectDump.txt", 'r') as d:
                                subjects = [line.rstrip('\n') for line in d]
                    else:
                        box = 0

                if 25 < mouse[1] < 50:
                    if width - 50 < mouse[0]:
                        if screen == 2:
                            screen = 3
                            box = 4
                            update = True
                        elif screen == 1:
                            screen = 2
                            box = 0
                            rawInput = ""
                            subjectInput = ""
                            timeInput = ""
                            update = True
                    elif 50 > mouse[0]:
                        if screen == 2:
                            screen = 1
                            box = 0
                            update = True
                        elif screen == 3:
                            screen = 2
                            box = 0
                            rawInput = ""
                            update = True

    pygame.display.update()
pygame.quit()
