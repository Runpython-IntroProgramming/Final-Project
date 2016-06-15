from ggame import App, Color, Sprite, RectangleAsset, LineStyle, TextAsset, MouseEvent, CircleAsset

red= Color(0xff0000, 1)
green= Color(0x228b22, 1)
black= Color(0X000000, 1)
outline= LineStyle(1, black)
nooutline= LineStyle(0, red)

class thechoice(Sprite):
    
    strings = {'single': 'Single Player!',
        'multi': '2 Players!',
        }
    
    def __init__(self, position):
        super().__init__(thechoice.dia, position)
        
        self.listenMouseEvent('click', self.decide)

class thechoice2(Sprite):
    
    strings = {'x': 'X',
        'o': 'O',
        }
        
    def __init__(self, position):
        super().__init__(thechoice2.dia, position)
        
        self.listenMouseEvent('click', self.decide)
        
class bloc(Sprite):
    pix= RectangularAsset(10,10,nooutline,

class tictactoe(App):

myapp = tictactoe(640, 480)
myapp.run()