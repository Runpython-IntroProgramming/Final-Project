#Ella Edmonds Final Project
#Fireboy and Water Girl

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

grey = Color(0x000000,.3)
gridline = LineStyle(1,grey)

class Game(App):
    def __init__(self):
        super.()__init__()
        grid = RectangleAsset(50,50,gridline,grey)
        x=0
        y=0
        for b in range(15):
            for a in range(25):
                Sprite(grid,(x,y))
                x=x+50
            y=y+50





myapp = App()
myapp.run()