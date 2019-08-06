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

    numb1 = 100
    numb2 = 10
    numb2 += 5
    text_pos = [numb1, numb2]

    #defining how to generate the random info
    newnumb = random.randint(0, 1000)
    choices = open('colors.txt', 'r')
    color = random.choices(choices.readlines())
    #printing the text out
    new_main = str(color) + str(newnumb)
    font = pygame.font.Font('arial.ttf', 16)
    text = font.render(new_main, True, (255, 255, 255))
    #surface for the text
    screen.blit(text, text_pos)
    pygame.display.update()

def resources():
    stresources = 10

    font = pygame.font.Font('arial.ttf', 16)
    resource = font.render(str(stresources), True, (0, 188, 0))
    repos = (600, 10)
    screen.blit(resource, repos)

    for stresources in range(100):
        stresources += 1
        screen.blit(resource, repos)
        time.sleep(10)

    pygame.display.update()

z = 0

while z < 7:
    main()
    resources()
    pygame.display.update()
    z += 1



for z in range(100000):
    pygame.display.update()
    time.sleep(10000)
