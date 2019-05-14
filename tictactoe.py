from ggame import App, ImageAsset, RectangleAsset, Sprite, LineStyle, Frame, Color

class Board(Sprite):
    asset = ImageAsset("images/Screen Shot 2019-05-13 at 2.49.49 PM.png")
    def __init__(self, position):
        super().__init__(Board.asset, position)
    #Sprite(asset, (0,0))

class exe(Sprite):
    asset = ImageAsset("images/x.png")
    width = 70
    height = 70
    def __init__(self, position):
        super().__init__(exe.asset, position)
        self.scale = .15
        self.mass = 30000
    Sprite(asset, (200,200))
       
class Game(App):
    def __init__(self):
        super().__init__()
        Board((0,0))
        self.height = 700
        self.width = 1200

myapp = Game()
myapp.run()