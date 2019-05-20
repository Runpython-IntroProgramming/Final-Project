from ggame import App, ImageAsset, RectangleAsset, Sprite, LineStyle, Frame, Color

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)


class Board(Sprite):
    asset = ImageAsset("images/Screen Shot 2019-05-13 at 2.49.49 PM.png")
    def __init__(self, position):
        super().__init__(Board.asset, position)

class exe(Sprite):
    asset = ImageAsset("images/X.png")
    def __init__(self, position):
        super().__init__(exe.asset, position)
        self.scale = .5

class owe(Sprite):
    asset = ImageAsset("images/O.png")
    def __init__(self, position):
        super().__init__(owe.asset, position)
        self.scale = .5

class horiz(Sprite):
    asset = RectangleAsset(450, 10, thinline, black)
    def __init__(self, position):
        super().__init__(horiz.asset, position)

class vert(Sprite):
    asset = RectangleAsset(10, 450, thinline, black)
    def __init__(self, position):
        super().__init__(vert.asset, position)
 

class diag1(Sprite):
    asset = RectangleAsset(10, 630, thinline, black)
    def __init__(self, position):
        super().__init__(diag1.asset, position)
        self.rotation = .785

class diag2(Sprite):
    asset = RectangleAsset(10, 630, thinline, black)
    def __init__(self, position):
        super().__init__(diag2.asset, position)
        self.rotation = -.785
        

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
        print("Welcome to Tic Tac Toe")
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
        self.if1 = 0
        self.if2 = 0
        self.if3 = 0
        self.if4 = 0
        self.if5 = 0
        self.if6 = 0
        self.if7 = 0
        self.if8 = 0
        self.if9 = 0
    def spot1(self, event):
        if self.turns % 2 == 0 and self.if1 == 0:
            exe((300,200))
            a = 5
            self.turns += 1
            self.if1 = 1
        elif self.turns % 2 == 1 and self.if1 == 0:
            owe((300,200))
            a = 7
            self.turns += 1
            self.if1 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot2(self, event):
        if self.turns % 2 == 0 and self.if2 == 0:
            exe((450,200))
            b = 5
            self.turns +=1
            self.if2 = 1
        elif self.turns % 2 == 1 and self.if2 == 0:
            owe((450,200))
            b = 7
            self.turns +=1
            self.if2 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot3(self, event):
        if self.turns % 2 == 0 and self.if3 == 0:
            exe((600,200))
            c = 5
            self.turns += 1
            self.if3 = 1
        elif self.turns % 2 == 1 and self.if3 == 0:
            owe((600,200))
            c = 7
            self.turns += 1
            self.if3 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot4(self, event):
        if self.turns % 2 == 0 and self.if4 == 0:
            exe((300,350))
            d = 5
            self.turns += 1
            self.if4 = 1
        elif self.turns % 2 == 1 and self.if4 == 0:
            owe((300,350))
            d = 7
            self.turns += 1
            self.if4 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot5(self, event):
        if self.turns % 2 == 0 and self.if5 == 0:
            exe((450,350))
            e = 5
            self.turns += 1
            self.if5 = 1
        elif self.turns % 2 == 1 and self.if5 == 0:
            owe((450,350))
            e = 7
            self.turns += 1
            self.if5 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot6(self, event):
        if self.turns % 2 == 0 and self.if6 == 0:
            exe((600,350))
            f = 5
            self.turns += 1
            self.if6 = 1
        elif self.turns % 2 == 1 and self.if6 == 0:
            owe((600,350))
            f = 7
            self.turns += 1
            self.if6 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot7(self, event):
        if self.turns % 2 == 0 and self.if7 == 0:
            exe((300,500))
            g = 5
            self.turns += 1
            self.if7 = 1
        elif self.turns % 2 == 1 and self.if7 == 0:
            owe((300,500))
            g = 7
            self.turns += 1
            self.if7 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot8(self, event):
        if self.turns % 2 == 0 and self.if8 == 0:
            exe((450,500))
            h = 5
            self.turns += 1
            self.if8 = 1
        elif self.turns % 2 == 1 and self.if8 == 0:
            owe((450,500))
            h = 7
            self.turns += 1
            self.if8 = 1
        else:
            print("Please choose another space")
        self.checkwinner()
    def spot9(self, event):
        if self.turns % 2 == 0 and self.if9 == 0:
            exe((600,500))
            i = 5
            self.turns += 1
            self.if9 = 1
        elif self.turns % 2 == 1 and self.if9 == 0:
            owe((600,500))
            i = 7
            self.turns += 1
            self.if9 = 1
        else:
            print("Please choose another space")
        self.checkwinner()

    def checkwinner(self):
        if a == 5 and b == 5 and c == 5:
            horiz((270,230))
            print("X Wins")
        elif d == 5 and e == 5 and f == 5:
            horiz((270,380))
            print("X Wins")
        elif g == 5 and h == 5 and i == 5:
            horiz((270,530))
            print("X Wins")
        elif a == 5 and d == 5 and g == 5:
            vert((340,160))
            print("X Wins")
        elif b == 5 and e == 5 and h == 5:
            vert((490,160))
            print("X Wins")
        elif c == 5 and f == 5 and i == 5:
            vert((640,160))
            print("X Wins")
        elif a == 5 and e == 5 and i == 5:
            diag1((270,160))
            print ("X Wins")
        elif c == 5 and e == 5 and g == 5:
            diag2((720,160))
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

myapp = Game()
myapp.run()