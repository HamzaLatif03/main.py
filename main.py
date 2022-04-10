import pygame
import random


pygame.init()
pygame.font.init()

sw = 1000
sh = 720


playerShip = pygame.image.load("Playership.png")
asteroids = pygame.image.load("asteroid.png")
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
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
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
        pygame.sprite.Sprite.__init__(self)
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

    def xCoordinate(self):
        return self.x
                
    def yCoordinate(self):
        return self.y
    
    def draw(self):
        if self.y < sh or  self.health == 0:
            self.alive == False
            if self.alive:
                screen.blit(enemyShip, (self.x, self.y))
                 
class Bullet():
    def __init__(self, x, y):
        self.x = x + 50
        self.y = y - 10
        self.image = laser
        self.rect = self.image.get_rect(center = (35,30))
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True
    
    def move(self):
        self.y -= 15
    
    def bulletState(self):
        return (self.y < -100)

    def collision(self):
        self.hits = pygame.sprite.spritecollide(self, eA, False)
        if self.hits:
            print("collide ")
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
                #pygame.time.delay(1) slow downs time potential power up
                
class Asteroids(Enemy):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroids
        self.x = x
        self. y = y
        self.alive = True
        self.direction = random.randint(0,1)
        
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
asteroidsScreen = Asteroids(500,0)
enemies= []
enemies.append(enemy)
     

allSprites = pygame.sprite.Group()
eA = pygame.sprite.Group()
eAS = pygame.sprite.Group()
B = pygame.sprite.Group()
P = pygame.sprite.Group()


for i in range(6):
    eA.add(enemy)
    allSprites.add(enemy)
allSprites.add(player)     
     

def redrawScreen():
    screen.blit(bg, (0,0))
    
        
    for enemy in enemies:
        enemy.draw()
        enemy.move()
            
    player.draw()
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.shoot(keys)
    asteroidsScreen.draw()
    asteroidsScreen.move()
    for bullet in player.bullets:
        bullet.collision()
        bullet.draw()
        
    pygame.display.update()
    

def game():
    global bg
    clock.tick(60)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        screen.blit(bg, (0,0))
        
        if not enemy.alive():
            enemy = Enemy(random.randint(100,750), random.randint(-50,-40)) 
        
        for i, inst in enumerate(eA):
            if inst.rect.y >= (sh - 50):
                score += 1
                inst.kill()
                enemy = Enemy(random.randint(100,750), random.randint(-50,-40)) 
                eA.add(enemy)
                allSprites.add(enemy)
        allSprites.draw(screen)
        allSprites.update()  
        
        redrawScreen()
        
game()
