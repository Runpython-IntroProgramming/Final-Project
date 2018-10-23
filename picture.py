from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xFF9494, 1)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, .3)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
tan = Color(0xFFFFE6, 1.0)
orange = Color(0xFFC300, 1.0)

line1 = LineStyle(1, black)
line0 = LineStyle(0, black)

background = RectangleAsset(1500, 1000, line0, tan)
Sprite(background)

leftbar = RectangleAsset(200, 1000, line0, red)
Sprite(leftbar, (10,60))

banner = RectangleAsset(1100, 50, line0, red)
Sprite(banner)


roof = PolygonAsset([(0,0), (100,-150), (200,0)], line1, green)
Sprite(roof, (400,50))

circlesky = CircleAsset(20, line1, white)
Sprite(circlesky, (480,150))

tree = EllipseAsset(50, 100, line1, green)
Sprite(tree, (800,200))

# add your code here /\  /\  /\

myapp = App()
myapp.run()
