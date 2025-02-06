import pygame

pygame.init()
width = 1024
height = 768

screen = pygame.display.set_mode((width, height))
screen.fill("black")

clock = pygame.time.Clock()

icon = pygame.image.load('bebebe.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Zdarova epta')

class Object:
    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = color

Box1 = Object([70, 80, 90, 100], "white")
Box2 = Object([600, 500, 220, 80], "white")
Box3 = Object([150, 600, 100, 140], "white")

Circle1 = Object([360, 240], "white")
Circle2 = Object([700, 250], "white")


speed = 3


x = 512
y = 400

displacement_up = False
displacement_down = False
displacement_right = False
displacement_left = False

running = True
while running:
    screen.fill("black")
    pygame.draw.rect(screen, Box1.color, Box1.coordinates)
    pygame.draw.rect(screen, Box2.color, Box2.coordinates)
    pygame.draw.rect(screen, Box3.color, Box3.coordinates)

    pygame.draw.circle(screen, Circle1.color, Circle1.coordinates, 60)
    pygame.draw.circle(screen, Circle2.color, Circle2.coordinates, 80)

    pygame.draw.circle(screen, "orange", [x, y], 10)

    pygame.display.flip()

    if displacement_down and y < height:
        y += speed
    if displacement_up and y > 0:
        y -= speed
    if displacement_left and x > 0:
        x -= speed
    if displacement_right and x < 1024:
        x += speed

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                displacement_up = True
            if event.key == pygame.K_a:
                displacement_left = True
            if event.key == pygame.K_s:
                displacement_down = True
            if event.key == pygame.K_d:
                displacement_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                displacement_up = False
            if event.key == pygame.K_a:
                displacement_left = False
            if event.key == pygame.K_s:
                displacement_down = False
            if event.key == pygame.K_d:
                displacement_right = False
    clock.tick(60)
