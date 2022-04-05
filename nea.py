import pygame
import math
import sys
import random
import menu_test

menu_test

pygame.font.init()

sw = 1150
sh = 1000


playerShip = pygame.image.load("PLAYER_SHIP.png")
asteroids = pygame.image.load("ASTEROID.png")
enemy = pygame.image.load("E_BOSS.png")
missile = pygame.image.load("F_WEAPON.png")
bg = pygame.image.load("BACKGROUND.png")

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Hamza's: Space game")

clock = pygame.time.Clock()

gameover = False

class Player:
    def __init__(self, health):
        self.ship_img = playerShip
        self.w = self.ship_img.get_width()
        self.h = self.ship_img.get_height()
        self.x = sw / 2
        self.y = sh / 2
        self.boost = 100
        self.initial_health = health
        self.remaining_health = health
        self.pos = (self.x, self.y)
        self.rect = self.ship_img.get_rect()
        self.when_shot = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.ship_img)

    def draw(self, screen):
        screen.blit(self.ship_img, (self.x, self.y, self.w, self.h))
        #screen.blit(self.x, self.y)
        pygame.draw.rect(screen, (255,0,0), (self.rect.x, (self.rect.bottom + 10), self.w, 15))
        if self.remaining_health > 0:
            pygame.draw.rect(screen, (0,255,0), (self.rect.x, (self.rect.bottom + 10), (self.w * (self.remaining_health / self.initial_health)), 15))            

    def move(self,keys):
        velocity = 5
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.x -= velocity
        elif keys[pygame.K_RIGHT] and self.rect.right < sw:
            self.x += velocity
        elif keys[pygame.K_DOWN] and self.rect.bottom < 0:
            self.y += velocity
        elif keys[pygame.K_UP] and self.rect.top > sh:
            self.y -= velocity
        elif keys[pygame.K_w]:
            Player.accelerate()

        time = pygame.time.get_ticks()

        #if keys[pygame.K_SPACE] and time - self.when_shot:
            #bullet = Bullet(self.x, self.y + 10)
            #bullet_group.add(bullet)
             

    def positionx(self):
       self.Rect.center_x = (self.x)


    def positiony(self):
       self.Rect.center_y = (self.y)

  
    def accelerate(self, keys, velocity, boost):
        a = 1.3
        if keys[pygame.K_w]:
            while boost > 0:
                self.x = velocity * a 
                self.y = velocity * a   

'''
class Bullet(Player):
    def __init__(self, x, y):
        self.missile_img = missile
        self.maxAmmo = 10
        self.shots = [0]
        self.num = 1
        self.x = Player.positionx()
        self.y = Player.positiony()
        self.v = 2
        self.w = 5
        self.h = 10
##        self.mask.pygame.mask.from_surface(self.missile_img)

    def draw(self, screen):
        pygame.draw.rect(bg, (255,255,255), [self.x, self.y, self.w, self.h])

    def shoot(self, keys):
        if Bullet.CanShoot == True:
            self.pos = player.pos
            if self.y >= sh + 100:
                self.kill(10)

            bullet.move()
        else:
            bullet.blank()

    def move(self):
        self.y += self.yv

    def UpdateBullet(self, num, shots):
        self.rect.y -= 5
        if self.missile_img.y >= sh + 100:
            self.kill()
            self.shots = shots.pop(self.num)
            self.num -= 1
            
    def CanShoot(self, shots, num):
        while confirm == " " :
            self.shots.append(self.num)
            self.num += 1
            self.long = len(self.shots) - 1
            if self.num > 4:
                CanShoot = False
            else:
                CanShoot = True
                
    def blank(self):
        while Bullet.CanShoot == False:
            shoot = False
            #playsound = click.mp3
'''
    #def draw(self,win):
    #    pygame.draw.rect(bg, (255, 255, 255), [self.x, self.y, self.w, self.h])
##        screen.blit(self.rotatedSurf,


player = Player(5)
#bullet = Bullet()
#playerBullets=[]

#Objects = pygame.sprite.Group()
#Objects.add(player)
#Objects.add(bullet)

def redraw_screen():
    screen.blit(bg, (0, 0))
    #Objects.draw(screen)
    player.draw(screen)
    #bullet.draw(screen)
    pygame.display.update()




def game():
    while True:
        for event in pygame.event.get():
            clock.tick(60)
            if not gameover:
                #for b in playerBullets:
                    #b.move()

                keys = pygame.key.get_pressed()
                player.move(keys)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


        redraw_screen()






'''
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet.shoot()
                    if not gameover:
                        playerBullets.append(Bullet())
    '''



'''
    FPS=60 
    hits=5
    score=0
    main_font= pygame.font.SysFont("comicsans", 50)
    lost_font= pygame.font.SysFont("comicsans", 70)

    velocity = 10

    enemies = []
    enemyVel = 5

    lost = False

    player = Player(300,650)

    clock = pygame.time.Clock()

    gameover = False
'''

'''


        if gameover :
            lost_label = lost_font.render("You have lost!", 1, (0,255,0))
            screen.blit(lost_label, (sw/2 - lost_label.get_width()/2, 350))



        pygame.display.update()

'''
#nice = pygame.transform.scale(nice, (100,100))
# good size for my asteroids in the game
# random.randint(n1, n2) can be used for asteroids to be random sizes with set limits