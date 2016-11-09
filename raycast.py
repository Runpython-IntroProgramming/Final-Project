from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

scrw= 640
scrh=480
SCREEN_WIDTH = scrw
SCREEN_HEIGHT = scrh

black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)

width=list(range(0,int((scrw/10))+1))
height = list(range(0,int((scrh/10))+1))
print(width)
print(height)
click = 0

colors={"0101":"0"}
for x in width:
    for y in height:
        colors['0'+str(x)+'0'+str(y)]=0

thinline = LineStyle(1, black)
rsquare_asset =RectangleAsset(10,10, thinline, red)
wsquare_asset = RectangleAsset(10, 10, thinline, white)
for x in width:
    for y in height:
        Sprite(wsquare_asset,(x*10, y*10))

