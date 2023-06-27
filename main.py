import pygame
import random
import math


def gameloop():
    # initialization
    pygame.init()
    # screen formation
    screen = pygame.display.set_mode((800, 600))
    # ICON AND CAPTION
    pygame.display.set_caption("SNAKE GAME")
    logo = pygame.image.load("snakes.png")
    pygame.display.set_icon(logo)
    # Background
    back = pygame.image.load("snakeBackground.png")
    # clock
    fps = 60
    clock = pygame.time.Clock()
    # snake
    snakeImg = pygame.image.load("snakebody.png")
    snakeX = 368
    snakeY = 300
    snXchng = 0
    snYchng = 0

    def snake(x, y):
        screen.blit(snakeImg, (x, y))

    # Food
    foodImg = pygame.image.load("apple.png")
    foodX = random.randint(250, 760)
    foodY = random.randint(200, 550)

    def food(x, y):
        screen.blit(foodImg, (x, y))

    # Collision
    def iscollision(snakeX, snakeY, foodX, foodY):
        d = math.sqrt((math.pow(snakeX - foodX, 2)) + (math.pow(snakeY - foodY, 2)))
        if d <= 22:
            return 5
        else:
            return 6

    # snake increement logic
    l = []
    a1 = 1

    def plt(l):
        for x, y in l:
            snake(x, y)

    # score
    score = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
    scoreX = 10
    scoreY = 10

    # ending and gameover
    f1 = pygame.font.Font("freesansbold.ttf", 32)
    eX = 60
    eY = 300

    def ending(x, y):
        e = font.render("GAME OVER PRESS RETURN TO PLAY AGAIN", True, (255, 255, 255))
        screen.blit(e, (x, y))

    def thegameover():
        for i in l[:-1]:
            if i == l1:
                return 7

    def showscore(x, y):
        sc = font.render("Score-->" + str(score), True, (255, 255, 255))
        screen.blit(sc, (x, y))

    ch = True
    while ch:
        gameover = thegameover()
        if gameover == 7:
            screen.fill((0, 0, 200))
            ending(eX,eY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ch = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()


        else:
            # RGB
            screen.fill((75, 240, 165))
            screen.blit(back, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ch = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snXchng = -10
                        snYchng = 0
                    if event.key == pygame.K_RIGHT:
                        snXchng = +10
                        snYchng = 0
                    if event.key == pygame.K_UP:
                        snYchng = -10
                        snXchng = 0
                    if event.key == pygame.K_DOWN:
                        snYchng = 10
                        snXchng = 0
            snakeX += snXchng  # snakeX=snakeX-snXchng
            snakeY += snYchng
            snake(snakeX, snakeY)
            food(foodX, foodY)
            showscore(scoreX, scoreY)
            col = iscollision(snakeX, snakeY, foodX, foodY)
            if col == 5:
                score = score + 10
                a1 += 2
                foodX = random.randint(250, 760)
                foodY = random.randint(200, 550)
                food(foodX, foodY)
            l1 = []
            l1.append(snakeX)
            l1.append(snakeY)
            l.append(l1)
            if len(l) > a1:
                del l[0]
            plt(l)
            if snakeX >= 780:
                snakeX = -10
            elif snakeX <= -10:
                snakeX = 780
            elif snakeY >= 580:
                snakeY = -10
            elif snakeY <= -10:
                snakeY = 580
        clock.tick(fps)
        pygame.display.update()


gameloop()
