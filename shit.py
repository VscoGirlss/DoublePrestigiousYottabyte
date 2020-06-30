import pygame

#Create ship call that takes in position
class Ship(pygame.sprite.Sprite):
  
  #create __init__ 
  def __init__(self,pos):
    super().__init_()
    #create the ship
    self.image = pygame.image.load ("ship.png")
    self.image = pygame.transform.smoothscale(self.image,(40,40))
    #rotate imagine
    self.image = pygame.transform.rotate(self.image,-90)
    self.rect = self.image.get_rect()
    #move cent of rectangle to funtion
    self.rect.center = pos
    #set print
    self.speed = pygame.math.Vector2(0,0)

  #create function to update
  def update(self):
    self.rect.move_i(self.speed)