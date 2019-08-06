import random
import pygame
import time

pygame.init()

width = 720
height = 700

size = width, height
speed = [2, 2]
black = [0, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 128]

screen = pygame.display.set_mode(size)


pygame.display.set_caption("Help")


def main():
    #equation for the y position on screen

    numb1 = random.randint(10, 150)
    numb2 = random.randint(1, 3)
    equat = (width/numb2) + numb1
    equat2 = (height/numb2) * 1.5
    text_pos = [equat, equat2]

    #defining how to generate the random info
    newnumb = random.randint(0, 1000)
    choices = open('colors.txt', 'r')
    color = random.choices(choices.readlines())
    #printing the text out
    new_main = str(color) + str(newnumb)
    font = pygame.font.Font('arial.ttf', 16)
    text = font.render(new_main, True, (255, 255, 255))
    #surface for the text

    stresources = 10
    blue = pygame.color("#8FD8D8")
    resources = font.render(stresources, True, blue)
    rePos = (350, 10)
    screen.blit(resources, rePos)


    while stresources <= 100:
        stresources += 1
        time.sleep(10)




    screen.blit(text, text_pos)
    pygame.display.update()




z = 0

while z <= 7:
    main()
    z += 1

else:
    pygame.displa.update()