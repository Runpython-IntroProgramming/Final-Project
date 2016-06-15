from ggame import App, Color, Sprite, RectangleAsset, LineStyle, TextAsset, MouseEvent, CircleAsset

white= Color(0xffffff, 1)
red= Color(0xff0000, 1)
green= Color(0x228b22, 1)
black= Color(0X000000, 1)
outline= LineStyle(1, black)
nooutline= LineStyle(0, red)

class thechoice(Sprite):
    
    strings = {'single': 'Single Player',
        'multi': '2 Players',
        }
    background= RectangleAsset(100,200,
    
    def __init__(self, position):
        super().__init__(thechoice.dia, position)
        
        self.listenMouseEvent('click', self.decide)

        if 