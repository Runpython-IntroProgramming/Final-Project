# Rain's final project
from math import sin, cos, pi
from ggame import App, Color, LineStyle, Sprite, CircleAsset

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

class SpaceShip(Sprite):
    def __init__(asset, xpen, ypen, app):
        R = float(input('Radius of circle 1: '))
        r = float(input('Radius of circle 2: '))
        xpen = (R-r)*cos(a) + r*50*cos(((R/r)-1)*a)+200
        ypen = (R-r)*sin(a) - r*50*sin(((R/r)-1)*a)+200
        asset = CircleAsset(.5, thinline, black)
        super().__init__(asset, xpen, ypen, app)
    
     def step(self):
        super().step()
        self.time += 1
        if self.time % 100 == 0:
            Bolt(self.direction, 
                 self.x+self.width//2,
                 self.y+10,
                 self.app)
            self.direction *= -1
            
myapp = App()
myapp.run()