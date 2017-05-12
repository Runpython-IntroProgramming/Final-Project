"""
when the motor is on (the vx is more than zero) and you point the nose in a direction, it will go in that direction.
when it is on the runway and the motor is not on, it will not move.
when it is on the runway, you control it through the wheels.
when you are up to a certain speed, it will take off.
you may not slow down the aircraft to a stop mid-flight(later on make it so it will nosedive instead).
you may not go more than 70 degrees straight up and you may not fly upside down or the aircraft will fall out of the sky or nosedive. (can use a function for this)





"""




from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650

class Field(Sprite):
    field=ImageAsset("images/field.jpg")

    def __init__(self, position):
         super().__init__(Field.field, position)
         self.vx=1
         self.vy=1
         self.vr=0
         self.scale=1.5

class AOA():
    def __init__(self, r):
        self.rotation = r
    def anglex(self):
        return (1 * math.cos(self.rotation))
    def angley(self):
        return (-1 * math.sin(self.rotation))
        
class Explosion(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)

    def __init__(self, position):
        super().__init__(Explosion.asset, position)
        self.image = 0
        self.center = (0.5, 0.56)
        
    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()
            
class NuclearExplosion(Sprite):
    
    asset = ImageAsset("images/7db0bd54cbd390ca9ccee6b132333292_explosion-clip-art-explosion-clipart-transparent-background_664-800.png")

    def __init__(self, position):
        super().__init__(NuclearExplosion.asset, position)
        self.center = (0.5, 1)
        self.image = 0
        self.scale = 0.2
        
    def step(self):
        # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()

class Bomb(Sprite):
    
    nuke = ImageAsset("images/nuke.png")
    
    def __init__(self, position):
        super().__init__(Bomb.nuke, position)
        self.vx = 0.8
        self.vy = 1.5
        self.center = (1.2, 0.04)
        self.scale = 0.08
        
    def explode(self):
        self.visible = False
        Explosion(self.position)
        
    def stop(self):
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0
        self.vr = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if (self.y > SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT
            self.explode()
            self.stop()
       
       
class Nuke(Sprite):
    
    nuke = ImageAsset("images/nuclearwarhead.png")
    
    def __init__(self, position):
        super().__init__(Nuke.nuke, position)
        self.vx = 0.8
        self.vy = 1.5
        self.center = (1.2, 0.04)
        self.scale = 0.05
        
    def explode(self):
        self.visible = False
        NuclearExplosion(self.position)
        
    def stop(self):
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0
        self.vr = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if (self.y > SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT
            self.explode()
            self.stop()
            
    
class Plane(Sprite):
    airplane = ImageAsset("images/fighter.png")
    def __init__(self, position):
        super().__init__(Plane.airplane, position)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.vr = 0
        self.scale = 0.3
        self.lift_off = 0
        self.rotation = 0.08
        self.nobrakes = True
        self.bombs = 0
        self.nukes = 0
        self.fxcenter = self.fycenter = 0.5
        Game.listenKeyEvent("keydown", "d", self.RunwayForward)
        Game.listenKeyEvent("keydown", "a", self.RunwayBrake)
        Game.listenKeyEvent("keydown", "left arrow", self.Up)
        Game.listenKeyEvent("keydown", "right arrow", self.Down)
        Game.listenKeyEvent("keyup", "right arrow", self.Stop)
        Game.listenKeyEvent("keyup", "left arrow", self.Stop)
        Game.listenKeyEvent("keydown", "r", self.Restart)
        Game.listenKeyEvent("keydown", "t", self.Autopilot)
        Game.listenKeyEvent("keydown", "b", self.Drop_bomb)
        Game.listenKeyEvent("keydown", "f", self.Air_Brakes)
        Game.listenKeyEvent("keyup", "f", self.No_Brakes)
        Game.listenKeyEvent("keydown", "n", self.Drop_Nuke)
        
    
    
    def step(self):
        if (self.lift_off > 1):
            self.rotation += self.vr
            if (self.vr < -0.1):
                self.vr = -0
            if (self.vr > 0.1):
                self.vr = 0
        angle=AOA(self.rotation)
        if (self.lift_off > 1):
            if self.nobrakes is True:
                self.ax = (2 * angle.anglex())
                self.ay = (2 * angle.angley())
            if (self.y < 640):
                self.ay += 0.03
            self.x += self.ax
            self.y += self.ay
        if self.vx == 0:
            self.lift_off = 0
        if self.vx < 0:
            self.vx = 0
        if (self.y > (SCREEN_HEIGHT - 3)):
            self.x += self.vx
        if (self.x > SCREEN_WIDTH):
            self.x = 0
        if (self.y > SCREEN_HEIGHT):
            self.y = SCREEN_HEIGHT
            self.explode()
            self.stop()
        if (self.rotation > 1.2) and (self.rotation < 4.71):
            self.y += 1.5
            self.ax = 0
        if (self.x < 0):
            self.x = SCREEN_WIDTH

            
    def stop(self):
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0
        self.vr = 0
    
    def explode(self):
        self.visible = False
        Explosion(self.position)
        
        
    def slow(self):
        self.ax = (self.ax - (self.ax *0.001))
        self.ay = (self.ay - (self.ay * 0.001))
        if self.ax <= 0:
                self.ax = 0
        if self.ay <= 0:
                self.ay = 0
                
    def bomb_drop(self):
        Bomb(self.position)
        
    def nuke_drop(self):
        Nuke(self.position)
        
        
    def RunwayForward(self, event):
        self.vx += 0.05
        self.lift_off +=0.05
    def RunwayBrake(self, event):
        if self.y > 640:
            if self.vx > 0:
                self.vx -= 2.5
                self.ax -= 2.5
    def Up(self, event):
        self.vr += 0.1
    def Down(self, event):
        self.vr -= 0.1
    def Stop(self, event):
        self.vr=0
    def Restart(self, event):
        self.x = 0
        self.y = ((650) - 1)
        self.stop()
        self.rotation = 0.05
        self.visible = True
        self.bombs = 0
        self.nukes = 0
    def Autopilot(self, event):
        self.rotation = 0
    def Drop_bomb(self, event):
        if (self.rotation > -0.2) and (self.rotation < 0.2):
            self.bombs += 1
            if self.bombs <= 8:
                self.bomb_drop()
    def Air_Brakes(self, event):
        if self.rotation == 0:
            self.slow()
            self.nobrakes = False
    def No_Brakes(self, event):
        self.nobrakes = True
    def Drop_Nuke(self, event):
        if (self.rotation > -0.2) and (self.rotation < 0.2):
            self.nukes += 1
            if self.nukes <= 2:
                self.nuke_drop()

class Game(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 2)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Field((0,0))
        runway_asset = RectangleAsset(590, 15, noline, black)
        runway = Sprite(runway_asset, (0, 635))
        Plane((0,650))

    def step(self):
        for nuke in self.getSpritesbyClass(Bomb):
            nuke.step()
        for nuke in self.getSpritesbyClass(Nuke):
            nuke.step()
        for airplane in self.getSpritesbyClass(Plane):
            airplane.step()
        for asset in self.getSpritesbyClass(Explosion):
            asset.step()
        for asset in self.getSpritesbyClass(NuclearExplosion):
            asset.step()
        
            
myapp = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()