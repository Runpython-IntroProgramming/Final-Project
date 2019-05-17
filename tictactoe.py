from ggame import App, ImageAsset, RectangleAsset, Sprite, LineStyle, Frame, Color

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)


class Board(Sprite):
    asset = ImageAsset("images/Screen Shot 2019-05-13 at 2.49.49 PM.png")
    def __init__(self, position):
        super().__init__(Board.asset, position)

class exe(Sprite):
    asset = ImageAsset("images/X.png")
    width = 70
    height = 70
    def __init__(self, position):
        super().__init__(exe.asset, position)
        self.scale = .5
        self.mass = 30000

class owe(Sprite):
    asset = ImageAsset("images/O.png")
    width = 70
    height = 70
    def __init__(self, position):
        super().__init__(owe.asset, position)
        self.scale = .5
        self.mass = 30000
    Sprite(asset, (200,200))


horiz = RectangleAsset(150, 10, thinline, black)
vert = RectangleAsset(10, 150, thinline, black)

class diag1(Sprite):
    asset = ImageAsset("diagonal 1.png")
    width = 70
    height = 70
    def __init__(self, position):
        super().__init__(diag1.asset, position)
        self.scale = .5
        self.mass = 30000 

class diag2(Sprite):
    asset = ImageAsset("diagonal 2.png")
    width = 70
    height = 70
    def __init__(self, position):
        super().__init__(diag2.asset, position)
        self.scale = .5
        self.mass = 30000 

a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
h = 1
i = 1

class Game(App):
    def __init__(self):
        super().__init__()
        self.height = 700
        self.width = 1200
        Board((0,0))
        Game.listenKeyEvent("keydown", "1", self.spot1)
        Game.listenKeyEvent("keydown", "2", self.spot2)
        Game.listenKeyEvent("keydown", "3", self.spot3)
        Game.listenKeyEvent("keydown", "4", self.spot4)
        Game.listenKeyEvent("keydown", "5", self.spot5)
        Game.listenKeyEvent("keydown", "6", self.spot6)
        Game.listenKeyEvent("keydown", "7", self.spot7)
        Game.listenKeyEvent("keydown", "8", self.spot8)
        Game.listenKeyEvent("keydown", "9", self.spot9)
        self.turns = 0
    def spot1(self, event):
        if self.turns % 2 == 0:
            exe((300,200))
            a = 5
            self.turns += 1
        else:
            owe((300,200))
            a = 7
            self.turns += 1
    def spot2(self, event):
        if self.turns % 2 == 0:
            exe((450,200))
            b = 5
            self.turns +=1
        else:
            owe((450,200))
            b = 7
            self.turns +=1
    def spot3(self, event):
        if self.turns % 2 == 0:
            exe((600,200))
            c = 5
            self.turns += 1
        else:
            owe((600,200))
            c = 7
            self.turns += 1
    def spot4(self, event):
        if self.turns % 2 == 0:
            exe((300,350))
            d = 5
            self.turns += 1
        else:
            owe((300,350))
            d = 7
            self.turns += 1
    def spot5(self, event):
        if self.turns % 2 == 0:
            exe((450,350))
            e = 5
            self.turns += 1
        else:
            owe((450,350))
            e = 7
            self.turns += 1
    def spot6(self, event):
        if self.turns % 2 == 0:
            exe((600,350))
            f = 5
            self.turns += 1
        else:
            owe((600,350))
            f = 7
            self.turns += 1
    def spot7(self, event):
        if self.turns % 2 == 0:
            exe((300,500))
            g = 5
            self.turns += 1
        else:
            owe((300,500))
            g = 7
            self.turns += 1
    def spot8(self, event):
        if self.turns % 2 == 0:
            exe((450,500))
            h = 5
            self.turns += 1
        else:
            owe((450,500))
            h = 7
            self.turns += 1
    def spot9(self, event):
        if self.turns % 2 == 0:
            exe((600,500))
            i = 5
            self.turns += 1
        else:
            owe((600,500))
            i = 7
            self.turns += 1


if a == 5 and b == 5 and c == 5:
    horiz((303,250))
    print("X Wins")
elif d == 5 and e == 5 and f == 5:
    horiz((303,400))
    print("X Wins")
elif g == 5 and h == 5 and i == 5:
    horiz((303,550))
    print("X Wins")
elif a == 5 and d == 5 and g == 5:
    vert((303,400))
    print("X Wins")
elif b == 5 and e == 5 and h == 5:
    vcert((303,400))
    print("X Wins")
elif c == 5 and f == 5 and i == 5:
    horiz((303,400))
    print("X Wins")
elif a == 5 and e == 5 and i == 5:
    diag1((303, 250))
    print ("X Wins")
elif c == 5 and e == 5 and g == 5:
    diag2((603, 250))
    print ("X Wins")
elif a == 7 and b == 7 and c == 7:
    horiz((303,250))
    print("O Wins")
elif d == 7 and e == 7 and f == 7:
    horiz((303,400))
    print("O Wins")
elif g == 7 and h == 7 and i == 7:
    horiz((303,550))
    print("O Wins")
elif a == 7 and d == 7 and g == 7:
    vert((303,400))
    print("O Wins")
elif b == 7 and e == 7 and h == 7:
    vcert((303,400))
    print("O Wins")
elif c == 7 and f == 7 and i == 7:
    horiz((303,400))
    print("O Wins")
elif a == 7 and e == 7 and i == 7:
    diag1((303, 250))
    print ("O Wins")
elif c == 7 and e == 7 and g == 7:
    diag2((603, 250))
    print ("O Wins")
    
'''
if turns % 2 = 0:
    if Game.listenKeyEvent("keydown", "1"):
        exe((303,200))
        a = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "2"):
        exe((303,200))
        b = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "3"):
        exe((303,200))
        c = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "4"):
        exe((303,200))
        d = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "5"):
        exe((303,200))
        e = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "6"):
        exe((303,200))
        f = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "7"):
        exe((303,200))
        g = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "8"):
        exe((303,200))
        h = 5
        turns += 1
    elif Game.listenKeyEvent("keydown", "9"):
        exe((303,200))
        i = 5
        turns += 1
    else:
        print("Please try Again")
else:
    if Game.listenKeyEvent("keydown", "1"):
        owe((303,200))
        a = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "2"):
        owe((303,200))
        b = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "3"):
        owe((303,200))
        c = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "4"):
        owe((303,200))
        d = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "5"):
        owe((303,200))
        e = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "6"):
        owe((303,200))
        f = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "7"):
        owe((303,200))
        g = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "8"):
        owe((303,200))
        h = 7
        turns += 1
    elif Game.listenKeyEvent("keydown", "9"):
        owe((303,200))
        i = 7
        turns += 1
    else:
        print("Please try Again")
'''

myapp = Game()
myapp.run()