from ggame import App, Color, Sprite, RectangleAsset, LineStyle, TextAsset

red= Color(0xff0000, 1)
green= Color(0x228b22, 1)
black= Color(0X000000, 1)

class thechoice:
    
    strings = {'single': 'Single Player!',
        'multi': '2 Players!',
        }

class tictactoe(App):

myapp = tictactoe(640, 480)
myapp.run()