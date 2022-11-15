import pygame
from pygame.locals import *
import random

size = width, height = (800, 700)
road_w = int(width/1.6)
road_h = int(height/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
score = 0
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
running = True
# set Windows size
screen = pygame.display.set_mode(size)

# set title of game
pygame.display.set_caption("Go Car")

# set text of game
font =pygame.font.SysFont('arial', 16)
text = font.render('Score : '+ str(score),True,black, white)
textRect = text.get_rect()
textRect.topleft = (10,10)

# set background color
screen.fill((60, 220, 0))

# apply changes
pygame.display.update()
pygame.display.flip()

# load player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load enemy
otherCar = pygame.image.load("otherCar.png")
otherCar_loc = otherCar.get_rect()
otherCar_loc.center = left_lane, height*0.2

while running :
    
    # animate enemy vehicle
    otherCar_loc[1] += 1
    if otherCar_loc[1] > height:
        if random.randint(0, 1) == 0:
            otherCar_loc.center = right_lane, -200
            score += 1
            font =pygame.font.SysFont('arial', 16)
            text = font.render('Score : '+ str(score),True,black, white)

        else:
            otherCar_loc.center = left_lane, -200
            score +=1
            font =pygame.font.SysFont('arial', 16)
            text = font.render('Score : '+ str(score),True, black, white)

    # end game
    if car_loc[0] == otherCar_loc[0] and otherCar_loc[1] > car_loc[1] - 250 and otherCar_loc[1] < car_loc[1] + 250:
        print(" Game Over!")
        break
    
    # event listners        
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
            if event.key in [K_w, K_UP]:
                car_loc = car_loc.move([0, -int(road_h/3)])
            if event.key in [K_s, K_DOWN]:
                car_loc = car_loc.move([0, int(road_h)/3])

    # draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2 - road_w/2, 0, road_w, height))
        
    # center line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height)
    )

    # left line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
    )

    # right line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
    )

    screen.blit(car, car_loc)
    screen.blit(text, textRect)
    screen.blit(otherCar, otherCar_loc)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()