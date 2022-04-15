import pygame
import random


pygame.init()
pygame.font.init()

sw = 1000
sh = 720


playerShip = pygame.image.load("Playership.png")
asteroids = pygame.image.load("asteroid.png")
smallAsteroids = pygame.transform.scale(pygame.image.load("asteroid.png"),(random.randint(35,50),random.randint(35,50)))
midAsteroids = pygame.transform.scale(pygame.image.load("asteroid.png"),(random.randint(90,100),random.randint(90,100)))
bigAsteroids = pygame.transform.scale(pygame.image.load("asteroid.png"),(random.randint(130,150),random.randint(130,150)))
enemyShip = pygame.image.load("enemt ship.png")
laser = pygame.transform.scale(pygame.image.load("laser.png"),(70,60))
bg = pygame.image.load("background.png")

#click = mixer.music.load("click.mp3")

player_mask = pygame.mask.from_surface(playerShip)
Enemy_mask = pygame.mask.from_surface(enemyShip)
laser_mask = pygame.mask.from_surface(laser)

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Hamza's: Space game")

clock = pygame.time.Clock()

gameover = False


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, health = 5):
        super(Player, self).__init__()
        self.x = x
        self.y = y
        self.rect = playerShip.get_rect()
        self.image = playerShip
        self.laser = laser
        self.health = health
        self.mask = pygame.mask.from_surface(self.image)
        self.w = playerShip.get_width()
        self.h = playerShip.get_height()
        self.boost = 100
        self.velocity = 7
        self.bullets =[]
        self.cooloff = 0
    
    def draw(self):
        screen.blit(playerShip, (self.x, self.y))
        
    def cooldown(self):
        if self.cooloff >= 7:
            self.cooloff = 0
        elif self.cooloff > 0:
            self.cooloff +=1
            
    def shoot(self, keys):
        player.cooldown()
        if keys[pygame.K_SPACE] and self.cooloff == 0:
            bullet = Bullet(self.x, self.y)
            self.bullets.append(bullet)
            self.cooloff = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.bulletState():
                self.bullets.remove(bullet) 
 
    def move(self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > -45:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x < sw - 145:
            self.x += self.velocity
        if keys[pygame.K_UP] and self.y > - 20:
            self.y -= self.velocity
        if keys[pygame.K_DOWN] and self.y < sh - 145:
            self.y += self.velocity
        
        
        
class Enemy(Player):
    def __init__(self, x, y,  health = 3):
        super(Enemy, self).__init__(x, y)
        self.image = enemyShip
        self.x = x
        self.y = y
        self.health = health
        self.velocity = random.randint(1,3)
        self.velocityX = random.randint(-4,4)
        self.num = 1
        self.alive = True
        self.rect = self.image.get_rect(center = (120, 63))
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def move(self):
        self.y += self.velocity
        if self.x > 0 and self.x < sw - 250:
            self.x += self.velocityX
        if self.x == 0 or self.x == 1 or self.x == 2 or self.x == 3 or self.x == 4:
            self.velocityX = self.velocityX * -1
        if self.x == 746 or self.x == 747 or self.x == 748 or self.x == 749 or self.x == 750:
            self.velocityX = self.velocityX * -1
    
    def draw(self):
        if self.y < sh or  self.health == 0:
            self.alive == False
            if self.alive:
                screen.blit(enemyShip, (self.x, self.y))
                

                 
class Bullet():
    def __init__(self, x, y):
        self.x = x + 50
        self.y = y - 10
        self.w = laser.get_width()
        self.h = laser.get_height()
        self.image = laser
        self.rect = self.image.get_rect(center = (35,30))
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True
    
    def move(self):
        self.y -= 15
    
    def bulletState(self):
        return (self.y < -100)

    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
                #pygame.time.delay(1) slow downs time potential power up

                
class Asteroids(Enemy):
    def __init__(self, x, y):
        self.image = asteroids
        self.w = asteroids.get_width()
        self.h = asteroids.get_height()
        self.x = x
        self. y = y
        self.alive = True
        self.direction = random.randint(0,1)
        
    def big(self, size):
        self.size = size
        if self.size == 1:
            self.image = smallAsteroids
        if self.size == 2:
            self.image = midAsteroids
        if self.size == 3:
            self.image = bigAsteroids
        
    def boundaries(self):
        if self.y > sh or self.y < 0:
            self.alive == False
        if self.x > sw or self.x < 0:
            self.alive == False    
    
    def move(self):
        if self.direction == 1:
            self.y += random.randint(5,10)
            self.x += random.randint(5,10)
        elif self.direction == 0:
            self.y += random.randint(5,10)
            self.x -= random.randint(5,10)
    

    def draw(self):
        if self.alive == True:
            screen.blit(self.image, (self.x, self.y))
    
 
player = Player(sw//2, sh//2)
enemy = Enemy(random.randint(100,750), random.randint(-50,-40)) 
asteroid = Asteroids(500,0)
enemies= []
asteroids = []
count = 0
enemies.append(enemy)
     
Esprites = pygame.sprite.Group()
Asprites = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allSprites.add(player)

def redrawScreen():
    screen.blit(bg, (0,0))
    
    for a in asteroids:
        a.draw(screen)
        a.move()
        
    for enemy in enemies:
        enemy.draw()
        enemy.move()
            
    player.draw()
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.shoot(keys)
    asteroid.draw()
    asteroid.move()
    for bullet in player.bullets:
        bullet.draw()
        
    pygame.display.update()
    


clock.tick(30)
count += 1
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
    if count % 50 == 0:
        ran = random.choice([1,1,1,2,3,3])
        asteroids.append(Asteroids(ran))
    
    player_center = playerShip.get_rect
     
        
    screen.blit(bg, (0,0))
        
        
        
    redrawScreen()
        


