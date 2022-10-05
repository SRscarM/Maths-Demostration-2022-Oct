'''
Author: Sourav
Date of Creation: 29/9/2022
Class: 10th
Section: A
'''

# importing modules
import pygame
import sys, os

pygame.init()

displayFont = pygame.font.Font(os.path.join("images","Roboto-Light.ttf"),20)

# screen variables
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

# variables
mainGame = True
fps = 1
clock = pygame.time.Clock()
images = {}

# colour variables
black = (0,0,0)
white = (255,255,255)

# game images
images['icon'] = pygame.image.load(os.path.join("images","icon.png")).convert_alpha()
images['bg'] = pygame.image.load(os.path.join("images","background.png")).convert_alpha()

# Classes
class Spiral:

    def __init__(self):
        self.radius = 10

        self.pointA = ((screenX/2),(screenY/2))
        self.pointB = (((screenX / 2)+ self.radius), (screenY / 2))

        self.lineStart = (0, (screenY / 2))
        self.lineEnd = (screenX, (screenY / 2))

        self.colour = white
        self.width = 1
        self.varHolder = 10

    def initSpiral(self):
        pygame.draw.line(screen, self.colour, self.lineStart, self.lineEnd, self.width)
        pygame.draw.circle(screen, self. colour, self.pointA, self.varHolder, self.width, draw_top_right=True, draw_top_left=True)

    def drawPointA(self):
        self.radius += self.varHolder

        pygame.draw.circle(screen, self.colour, self.pointA, self.radius, self.width, draw_top_right=True, draw_top_left=True)
        pygame.display.update()

    def drawPointB(self):
        self.radius += self.varHolder

        pygame.draw.circle(screen, self.colour, self.pointB, self.radius, self.width, draw_bottom_right=True, draw_bottom_left=True)
        pygame.display.update()


class Processor:

    def __init__(self):
        self.pi = 22 / 7

    def takingInput(self,radius):
        self.numSpirals = int(input("Enter the number of Spirals: "))
        self.totalSum = (self.numSpirals / 2) * (2 * (radius) + (self.numSpirals - 1) * (radius))
        self.totalLength = self.pi * (self.totalSum)
        print(self.totalLength)

# objects
spiral = Spiral()
inputObject = Processor()

# defining icon and title
pygame.display.set_caption('Maths Demonstration - Arithmetic Progression')
pygame.display.set_icon(images['icon'])

def showText(n,m):
  textImageOne = displayFont.render(("Number of Semi-circles: " + str(round(n, 2))), True, white)
  textImageTwo = displayFont.render(("Total Length: " + str(round(m, 2)) + " cm"), True, white)

  screen.blit(textImageOne,(20,20))
  screen.blit(textImageTwo, (20, 60))

  pygame.display.update()


reset = False

while True:
    inputObject.takingInput(spiral.radius)
    numberOfSpirals = inputObject.numSpirals
    numberOfSpirals -= 1
    spiral.radius = spiral.varHolder

    # game loop
    screen.blit(images['bg'], (0, 0))
    showText(numberOfSpirals + 1, inputObject.totalLength)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    while mainGame:

        spiral.initSpiral()
        reset = False

        if numberOfSpirals >= 1:
            spiral.drawPointB()
            numberOfSpirals -= 1

            if numberOfSpirals >= 1:
                spiral.drawPointA()
                numberOfSpirals -= 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    reset = True

        clock.tick(fps)
        pygame.display.update()

        if reset == True:
            break




