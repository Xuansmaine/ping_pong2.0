from time import time as timer
#from random import *
from pygame import *

paddle = "fire.png"
background = "lab1.jpg"
ball = "sodium.png"
lose  = "explode2.png"


back = (0,0,0)
window_width = 700
window_height = 700
window = transform.scale(image.load("lab1.jpg"),(window_width,window_height))
window.fill(back)

clock = time.Clock()
FPS = 60


game = True
ball_speed = 1.05

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False


    class GameSprite(sprite.Sprite):
        def __init__ (self,player_image,player_x,player_y,size_x,size_y,player_speed):
            sprite.Sprite.__init__(self)

            self.image = transform.scale(image.load(player_image),(size_x,size_y))
            self.speed = player.speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        def reset(self):
            window.blit(self.image,(sel.rect.x,self.rect.y))

    class player(GameSprite):
        def update1(self): #player 1
            keys = key.get_pressed()
            if keys[K_s] and self.rect.y < window_height:
                self.rect.y += self.speed  
                
            if keys[K_w] and self.rect.y < window_height -80:
                self.rect.y -= self.speed

        def update2(self): #player 2
            keys = keyUp.get_pressed()
            if keys[K_UP] and self.rect.y <  window_height:
                self.rect.y += self.speed  
                
            if keys[K_DOWN] and self.rect.y < window_height -80:
                self.rect.y -= self.speed















            


    player1 = player( paddle , 30 , window_height/2 , 70 , 70, 10)
    player2 = player( paddle ,window_width-30 , window_height/2 , 70 , 70, 10)

    ping_pong = Balls( ball, window_width /2 , window_height /2, 50 , 50 , ball_speed )




















    player1.reset()
    player2.reset()
    ball.reset()




    display.update()
    clock.tick(FPS)
