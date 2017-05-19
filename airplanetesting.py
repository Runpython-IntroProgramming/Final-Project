"""
make the screen move
make a homing missile/turret
make the turning animation for Autopilot even more realistic
make a boost
make it more challenging
make a reusable explosion???
bomb going out of boundries doesn't explode?
add comments

0 to -3.05

6.33 to 9.48




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
         self.vy=0
         self.vr=0
         self.scale = 1.5


class bombCounter(Sprite):
    bomb_icon = ImageAsset("images/nuke.png")
    
    def __init__(self, position):
        super().__init__(bombCounter.bomb_icon, position)
        self.scale = 0.05
        self.visible = True
        self.rotation = 1.57
        Game.listenKeyEvent("keydown", "r", self.Reload)
    def Reload(self, event):
        self.visible = True
        
class nukeCounter(Sprite):
    nuke_icon = ImageAsset("images/nuclearwarhead.png")
    
    def __init__(self, position):
        super().__init__(nukeCounter.nuke_icon, position)
        self.scale = 0.032
        self.visible = True
        self.rotation = 1.57
        Game.listenKeyEvent("keydown", "r", self.Reload)
    def Reload(self, event):
        self.visible = True
        

class Tank(Sprite):
    base_tank = ImageAsset("images/15153-illustration-of-an-army-tank-pv.png")
    
    def __init__(self, position):
        super().__init__(Tank.base_tank, position)
        self.vx = 1
        self.vy = 0
        self.vr = 0
        self.scale = 0.1
        self.visible = True
        self.fxcenter = self.fycenter = 0.5
        Game.listenKeyEvent("keydown", "p", self.Restart)
        Game.listenKeyEvent("keydown", "u", self.Restart)


    def step(self):
        #self.x += self.vx
        nukeCollision = self.collidingWithSprites(NuclearExplosion)
        if len(nukeCollision) > 0:
            self.visible = False
        bombCollision = self.collidingWithSprites(Explosion)
        if len(bombCollision) > 0:
            self.visible = False
        planeCollision = self.collidingWithSprites(Plane)
        if len(planeCollision) > 0:
            self.visible = False
    def Restart(self, event):
        self.visible = True

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
        self.scale = 0.25
    def step(self):
        # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()

class Bomb(Sprite):
    
    nuke = ImageAsset("images/nuke.png")
    
    def __init__(self, position):
        super().__init__(Bomb.nuke, position)
        self.vx = 0
        self.vy = 0
        self.center = (0.5, 0.5)
        self.scale = 0.08
        self.visible = False
        Game.listenKeyEvent("keydown", "b", self.Mid_Air)
        self.variablememes = 0
    def explode(self):
        self.center = (0.5, 0.5)
        self.visible = False
        Explosion(self.position)
        self.variablememes = 0
        
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
            if self.visible == True:
                self.explode()
                self.stop()
        explosionCollision = self.collidingWithSprites(NuclearExplosion)
        if self.visible == True:
            if len(explosionCollision) > 0:
                self.visible = False
                self.stop()
                self.explode()
        if (self.x > SCREEN_WIDTH):
            self.x = 0
        
        
    def Mid_Air(self, event):
        self.variablememes += 1
        if self.variablememes == 2:
            if self.visible == True:
                self.explode()
                self.variablememes = 0
    
class GuidedBomb(Sprite):
    
    nuke = ImageAsset("images/nuke.png")
    
    def __init__(self, position):
        super().__init__(GuidedBomb.nuke, position)
        self.vx = 1.5
        self.vy = 1
        self.center = (0.5, 0.5)
        self.scale = 0.08
        self.visible = False
        self.rotation = 4.71
        Game.listenKeyEvent("keydown", "h", self.Mid_Air)
        Game.listenKeyEvent("keydown", "k", self.Left)
        Game.listenKeyEvent("keydown", "l", self.Right)
        
    def explode(self):
        self.center = (0.5, 0.5)
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
            if self.visible == True:
                self.explode()
                self.stop()
        explosionCollision = self.collidingWithSprites(NuclearExplosion)
        if len(explosionCollision) > 0:
            self.visible = False
            self.stop()
            self.explode()
        
    def Mid_Air(self, event):
        if self.visible == True:
            self.explode()
    def Left(self, event):
        self.vx -= (self.vx + 0.4)
    def Right(self, event):
        self.vx += (0.7)

class Nuke(Sprite):
    
    nuke = ImageAsset("images/nuclearwarhead.png")
    
    def __init__(self, position):
        super().__init__(Nuke.nuke, position)
        self.vx = 0.8
        self.vy = 1.5
        self.center = (1.2, 0.04)
        self.scale = 0.05
        self.visible = False
        self.variablememes = 0
        Game.listenKeyEvent("keydown", "n", self.Mid_Air)
        
    def explode(self):
        self.visible = False
        NuclearExplosion(self.position)
        self.variablememes = 0
        
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
            if self.visible == True:
                self.explode()
                self.stop()
        if (self.x > SCREEN_WIDTH):
            self.x = 0
    
    def Mid_Air(self, event):
        self.variablememes += 1
        if self.variablememes == 2:
            if self.visible == True:
                self.explode()
                self.variablememes = 0
        
    
class Plane(Sprite):
    airplane = ImageAsset("images/fighter.png")
    
    def __init__(self, position, bomb_name_list, nuke_name_list, bomb_icon_list, nuke_icon_list, guided_bomb_list):
        super().__init__(Plane.airplane, position)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.vr = 0
        self.scale = 0.3
        self.lift_off = 0
        self.rotation = 0.1
        self.nobrakes = True
        self.bombs = 0
        self.nukes = 0
        self.create = 0
        self.detroit = False
        self.boston = 0
        self.fxcenter = self.fycenter = 0.5
        self.collide = 0
        self.collisionMeme = False
        self.mynamejeff = False
        self.visibility_of_nuke = False
        self.humane = False
        self.variablememes = 0
        self.xy_multiplier = 3
        Game.listenKeyEvent("keydown", "d", self.RunwayForward)
        Game.listenKeyEvent("keydown", "a", self.RunwayBrake)
        Game.listenKeyEvent("keydown", "left arrow", self.Up)
        Game.listenKeyEvent("keydown", "right arrow", self.Down)
        Game.listenKeyEvent("keyup", "right arrow", self.Stop)
        Game.listenKeyEvent("keyup", "left arrow", self.Stop)
        Game.listenKeyEvent("keydown", "p", self.Restart)
        Game.listenKeyEvent("keydown", "t", self.Autopilot)
        Game.listenKeyEvent("keydown", "b", self.Drop_bomb)
        Game.listenKeyEvent("keydown", "f", self.Air_Brakes)
        Game.listenKeyEvent("keyup", "f", self.No_Brakes)
        Game.listenKeyEvent("keydown", "n", self.Drop_Nuke)
        Game.listenKeyEvent("keydown", "up arrow", self.Up_fine)
        Game.listenKeyEvent("keydown", "down arrow", self.Down_fine)
        Game.listenKeyEvent("keyup", "down arrow", self.Stop)
        Game.listenKeyEvent("keyup", "up arrow", self.Stop)
        Game.listenKeyEvent("keydown", "r", self.Reload)
        Game.listenKeyEvent("keydown", "z", self.Boost)
        Game.listenKeyEvent("keyup", "z", self.StopBoost)
        Game.listenKeyEvent("keydown", "m", self.Drop_GuidedBomb)
        self.bomb_icons = bomb_icon_list
        self.nuke_icons = nuke_icon_list
        self.bomb_name_list = bomb_name_list
        self.nuke_name_list = nuke_name_list
        self.guided_bomb_list = guided_bomb_list
    
    def step(self):
        newbomb = self.bomb_name_list[0]
        self.mynamejeff = newbomb.visible
        newnuke = self.nuke_name_list[0]
        self.visibility_of_nuke = newnuke.visible
        if (self.lift_off > 1):
            self.rotation += self.vr
            if (self.vr < -0.1):
                self.vr = -0
            if (self.vr > 0.1):
                self.vr = 0
        angle=AOA(self.rotation)
        if (self.lift_off > 1):
            if self.nobrakes is True:
                self.ax = (self.xy_multiplier * angle.anglex())
                self.ay = (self.xy_multiplier * angle.angley())
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
        nuke_explosionCollision = self.collidingWithSprites(NuclearExplosion)
        if len(nuke_explosionCollision) > 0:
            self.visible = False
        bomb_explosionCollision = self.collidingWithSprites(Explosion)
        if len(bomb_explosionCollision) > 0:
            self.visible = False
        tankCollision = self.collidingWithSprites(Tank)
        if len(tankCollision) > 0:
            self.visible = False
            self.explode()
            self.stop()
        if self.collisionMeme == True:
            self.collide += 1
            if self.collide == 18:
                bombCollision = self.collidingWithSprites(Bomb)
                if len(bombCollision) > 0:
                    self.visible = False
                    self.explode()
                    self.stop()
                    self.collide = 0
                    self.collisionMeme = False
        if (self.detroit is True) and self.boston < 140:
            self.boston += 1
            if (0 < self.rotation < 3.14):
                if (-0.10 < self.rotation < 0.10) is False:
                    self.rotation -= 0.03
                if (-0.10 < self.rotation < 0.10) is True:
                    self.rotation = 0
            if (3.14 < self.rotation < 6.283):
                if (-0.10 < self.rotation < 0.10) is False:
                    self.rotation += 0.03
                if (-0.10 < self.rotation < 0.10) is True:
                    self.rotation = 0
            if (0 > self.rotation > -3.14) is True:
                if (-0.10 < self.rotation < 0.10) is False:
                    self.rotation += 0.03
                if (-0.10 < self.rotation < 0.10) is True:
                    self.rotation = 0
            if -3.14 > self.rotation:
                self.rotation = 0
            if self.rotation > 6.284:
                self.rotation = 0
        if self.bombs < 7:
            bomb_icon1 = self.bomb_icons[0]
            bomb_icon2 = self.bomb_icons[1]
            bomb_icon3 = self.bomb_icons[2]
            bomb_icon4 = self.bomb_icons[3]
            bomb_icon5 = self.bomb_icons[4]
            bomb_icon6 = self.bomb_icons[5]
            if (self.bombs == 1):
                bomb_icon6.visible = False
            if (self.bombs == 2):
                bomb_icon6.visible = False
                bomb_icon5.visible = False
            if (self.bombs == 3):
                bomb_icon6.visible = False
                bomb_icon5.visible = False
                bomb_icon4.visible = False
            if (self.bombs == 4):
                bomb_icon6.visible = False
                bomb_icon5.visible = False
                bomb_icon4.visible = False
                bomb_icon3.visible = False
            if (self.bombs == 5):
                bomb_icon6.visible = False
                bomb_icon5.visible = False
                bomb_icon4.visible = False
                bomb_icon3.visible = False
                bomb_icon2.visible = False
            if (self.bombs == 6):
                bomb_icon6.visible = False
                bomb_icon5.visible = False
                bomb_icon4.visible = False
                bomb_icon3.visible = False
                bomb_icon2.visible = False
                bomb_icon1.visible = False
        if self.nukes < 3:
            nuke_icon1 = self.nuke_icons[1]
            nuke_icon2 = self.nuke_icons[0]
            if (self.nukes == 1):
                nuke_icon1.visible = False
            if (self.nukes == 2):
                nuke_icon1.visible = False
                nuke_icon2.visible = False

    def stop(self):
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0
        self.vr = 0
    
    def explode(self):
        self.visible = False
        Explosion(self.position)
        self.x = 0
        self.y = 0
        
    
    def slow(self):
        self.ax = (self.ax - (self.ax *0.001))
        self.ay = (self.ay - (self.ay * 0.001))
        if self.ax <= 0:
                self.ax = 0
        if self.ay <= 0:
                self.ay = 0
                
    def bomb_drop(self):
        newbomb = self.bomb_name_list[0]
        if newbomb.visible == False:
            newbomb.visible = True
            newbomb.vx = self.ax
            newbomb.vy = 2
            newbomb.x = (self.x - 50)
            newbomb.y = (self.y + 21)
            self.mynamejeff = newbomb.visible
        
    def guided_bomb_drop(self):
        newbomb = self.guided_bomb_list[0]
        if newbomb.visible == False:
            newbomb.visible = True
            newbomb.position = (self.position)

    def nuke_drop(self):
        newnuke = self.nuke_name_list[0]
        if newnuke.visible == False:
            newnuke.visible = True
            newnuke.vx = self.ax
            newnuke.vy = 2
            newnuke.position = (self.position)
            self.visibility_of_nuke = newnuke.visible
            
    def RunwayForward(self, event):
        self.vx += 0.05
        self.lift_off +=0.05
    def RunwayBrake(self, event):
        if self.y > 640:
            if self.vx > 0:
                self.vx -= 2.5
                self.ax -= 2.5
    def Up(self, event):
        if (self.lift_off > 1):
            self.vr += 0.05
    def Down(self, event):
        if (self.lift_off > 1):
            self.vr -= 0.05
    def Up_fine(self, event):
        self.vr += 0.007
    def Down_fine(self, event):
        self.vr -= 0.007
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
        self.detroit = True
        self.boston = 0
    def Drop_bomb(self, event):
        self.collisionMeme = True
        if self.mynamejeff == False:
            if self.visible == True:
                if (self.rotation > -0.2) and (self.rotation < 0.2):
                    self.bombs += 1
                    if self.bombs <= 8:
                        self.bomb_drop()
                        self.variablememes = 0
    def Drop_GuidedBomb(self, event):
        if self.visible == True:
            if (self.rotation > -0.2) and (self.rotation < 0.2):
                self.guided_bomb_drop()
    def Air_Brakes(self, event):
        if self.rotation == 0:
            self.slow()
            self.nobrakes = False
    def No_Brakes(self, event):
        self.nobrakes = True
    def Drop_Nuke(self, event):
        if self.visibility_of_nuke == False:
            if self.visible == True: 
                if (self.rotation > -0.2) and (self.rotation < 0.2):
                    self.nukes += 1
                    if self.nukes <= 2:
                        self.nuke_drop()
    def Reload(self, event):
        self.bombs = 0
        self.nukes = 0
    def Boost(self, event):
        self.xy_multiplier = 15
    def StopBoost(self, event):
        self.xy_multiplier = 3

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
        Tank((900,642))
        nuke_1 = Nuke((0,0))
        nuke_2 = Nuke((0,0))
        nuke_name_list = (nuke_1, nuke_2)
        bomb_1 = Bomb((0,0))
        bomb_2 = Bomb((0,0))
        guidedBomb = GuidedBomb((0,0))
        guided_bomb_list = (guidedBomb)
        bomb_name_list = (bomb_1, bomb_2)
        nuke_icon1 = nukeCounter((180,45))
        nuke_icon2 = nukeCounter((205,45))
        nuke_icon_list = (nuke_icon1, nuke_icon2)
        bomb_icon1 = bombCounter((25,40))
        bomb_icon2 = bombCounter((50,40))
        bomb_icon3 = bombCounter((75,40))
        bomb_icon4 = bombCounter((100,40))
        bomb_icon5 = bombCounter((125,40))
        bomb_icon6 = bombCounter((150,40))
        bomb_icon_list = (bomb_icon1, bomb_icon2, bomb_icon3, bomb_icon4, bomb_icon5, bomb_icon6)
        Plane((0,650), bomb_name_list, nuke_name_list, bomb_icon_list, nuke_icon_list, guided_bomb_list)
        
    def step(self):
        for nuke in self.getSpritesbyClass(Bomb):
            nuke.step()
        for nuke in self.getSpritesbyClass(GuidedBomb):
            nuke.step()
        for nuke in self.getSpritesbyClass(Nuke):
            nuke.step()
        for airplane in self.getSpritesbyClass(Plane):
            airplane.step()
        for asset in self.getSpritesbyClass(Explosion):
            asset.step()
        for asset in self.getSpritesbyClass(NuclearExplosion):
            asset.step()
        for base_tank in self.getSpritesbyClass(Tank):
            base_tank.step()
            
myapp = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()