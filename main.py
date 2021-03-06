#main file
import sys, pygame
from ship import*
from pygame.locals import*

pygame.init()
screen_info = pygame.display.Info()

#set the width and height to the size of the screen
size = (width,height) = (int(screen_info.current_w*0.5),int(screen_info.current_h*0.5))
screen = pygame.display.set_mode(size)

#create clock object
clock = pygame.time.Clock()
#create color RGB
color = (30,0,30)
#fill screen with color
screen.fill(color)

#setup game variables
NumLevels = 4
Level = 1
AsteroidCount = 3
Player = Ship((20,200))

#create main function
def main():
  global Level

  while Level <= NumLevels:
    #set our maximum refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      #Check if key being pressed down
      if event.type == pygame.KEYDOWN:
        #Check if it is right arrow
        if event.key == pygame.K_RIGHT:
          #If right arrow set x speed to 10(moving to right)
          Player.speed[0] = 10
        #Check if it is left arrow
        if event.key == pygame.K_LEFT:
          #If left arrow set x speed to -10(moving to left)
          Player.speed[0] = -10
        if event.key == pygame.K_UP:
          Player.speed[1] = -10
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 10
      #Check if key is released
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          #If right arrow set x speed to 0(stop moving)
          Player.speed[0] = 0
        #Check if it is left arrow
        if event.key == pygame.K_LEFT:
          #If left arrow set x speed to 0(stop moving)
          Player.speed[0] = 0
        if event.key == pygame.K_UP:
          Player.speed[1] = 0
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 0
    Player.update()
    #set screen color
    screen.fill(color)
    #add in ship image
    screen.blit(Player.image,Player.rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()