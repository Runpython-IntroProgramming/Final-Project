from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 570
myapp=App()
generation = False

primelist=[1]

a = 2


   
def spaceKey(event):
    MAX = int(input("How many primes should I count? "))
    i = 0
    global a
    
    while i !=MAX:
        b = 0
        for x in primelist:
            if int(a)%int(x) == 0:
                b += 1
                
        if b == 1:
            primelist.append(a)
            a += 1
            
            i+=1
        else:              
            a+=1
            
    print(primelist)
myapp.listenKeyEvent('keydown', 'space', spaceKey)


    
    

myapp.run()