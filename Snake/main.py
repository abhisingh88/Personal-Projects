import random
import pygame
import os

pygame.mixer.init()

pygame.init()



# colors
white = (255 , 255 , 255)
red = (255,0,0)
black = (0,0,0,)

screen_height = 900
screen_width = 600

gameWindow=pygame.display.set_mode((screen_height,screen_width))

# background image
bgImage=pygame.image.load("snake.jpg")
bgImage=pygame.transform.scale(bgImage,(screen_height,screen_width)).convert_alpha()

pygame.display.set_caption("SnakesBar")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)


def text_screen(text,color,x,y):
    screen_text= font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow, color, snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [ x , y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,220,229))
        text_screen("Welcome to SnakesBar",black,185,200)
        text_screen("Press SpaceBar to Play",black,190,240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # to play the music just before calling gameloop function
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameLoop()

        pygame.display.update()
        clock.tick(60)

# Creating a game loop
def gameLoop():
    # game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_length = 1
    snake_list = []

    # checks if highScore file exist or not
    if (not os.path.exists("highScore.txt")):
        with open("highScore.txt","w") as f:
            f.write("0")

    with open("highScore.txt", "r") as f:
        highScore = f.read()

    while not exit_game:
        if game_over:
            with open("highScore.txt", "w") as f:
                f.write(str(highScore))
            gameWindow.fill(white)
            text_screen("Game Over!! Press Enter to continue",red,100,200)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity                 #by default pygame follow convention as velocity is negative in +y direction

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

                    if event.key == pygame.K_q:
                        score+=10

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x) < 8 and abs(snake_y-food_y)<8:
                score+=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length += 5
                if score > int(highScore):
                    highScore=score

            gameWindow.fill(white)
            gameWindow.blit(bgImage,(0,0))
            # calling the function for printing the text on screen
            text_screen("Score: " + str(score)+ "  Highscore: "+str(highScore), red, 5, 5)

            # for printing the food on screen
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            #to manage/define the head part intially
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            #to control the length of snake after increment
            if len(snake_list) > snake_length:
                del snake_list[0]

            #to end the game if snake collid with itself
            if head in snake_list[:-1]:
                game_over=True
                # to play the diffrent music just before calling gameloop function
                pygame.mixer.music.load('back.mp3')
                pygame.mixer.music.play()

            #to end the game if snake collid with any side of the wall
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                # to play the diffrent music just before calling gameloop function
                pygame.mixer.music.load('back.mp3')
                pygame.mixer.music.play()
                game_over=True

            # for printing the snake on screen
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snake_list,snake_size)

        # at last you have to update the screen
        pygame.display.update()

        # for updating the screen per second
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()