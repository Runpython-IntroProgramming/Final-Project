from ggame import App, Color, Sprite, RectangleAsset, LineStyle, TextAsset, MouseEvent, CircleAsset

red= Color(0xff0000, 1)
green= Color(0x228b22, 1)
black= Color(0X000000, 1)
outline= LineStyle(1, black)
nooutline= LineStyle(0, red)

class tictactoe(App):
    
    strings= {'winner': 'WINNER!',
        'loser': 'LOSER!',
        'red': 'Click here for red',
        'green': 'Click here for green',
        }
        
app = tictactoe(0,0)
app.run()