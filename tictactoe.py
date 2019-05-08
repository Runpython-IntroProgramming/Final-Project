from ggame import App, ImageAsset, RectangleAsset, Sprite, LineStyle, Frame, Color

class Board(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    width = 500
    height = 500
    def __init__(self, position):
        super().__init__(Stars.asset, position)