from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
up=0
speed=3
blue=Color(0x87cefa, 1)
purple=Color(0x7b68ee, 1)
line=LineStyle(0,blue)
white = Color(0xfffafa,1)
green = Color(0x00ff00, 1)
black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, line, black)
bg = Sprite(bg_asset, (0,0))

snake=Sprite(RectangleAsset(15,15,line,purple),(25,25))
snake.dir=0
snake.go = True    

def leftKey(event):
    global up
    snake.dir=-speed
    up=0
def rightKey(event):
    global up
    snake.dir=speed
    up=0    
def upKey(event):
    global up
    snake.dir=-speed
    up=1
def downKey(event):
    global up
    snake.dir=speed
    up=1
def step():
    global up
    if snake.go:
        if up==0:
            snake.x += snake.dir
        if up==1:
            snake.y += snake.dir


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run(step)
myapp.listenKeyEvent('keydown', 'j', leftKey)
myapp.listenKeyEvent('keydown', 'i', upKey)
myapp.listenKeyEvent('keydown', 'k', downKey)
myapp.listenKeyEvent('keydown', 'l', rightKey)
