from ggame import App, ImageAsset, RectangleAsset, Sprite, LineStyle, Frame, Color

class Board(Sprite):
    asset = ImageAsset("images/Screen Shot 2019-05-07 at 2.54.32 PM.png")
    def __init__(self, position):
        super().__init__(Board.asset, position)
    Sprite(asset, (0,0))

class SpaceGame(App):
    def __init__(width, height):
        super().__init__()
        Board = Board((0,0))

myapp = App()
myapp.width = 1200
myapp.height = 700
myapp.run()