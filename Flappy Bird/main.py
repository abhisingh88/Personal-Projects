import random
import sys
import pygame
from pygame.locals import *

# Global variables for the game

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "gallery/images/bird.png"
BACKGROUND = "gallery/images/background.png"
PIPE = "gallery/images/pipe.png"


def welcomeScreen():
    """
    shows welcome images on the screen
    """
    playerx = int(SCREENWIDTH / 5)
    playery = int((SCREENHEIGHT - GAME_SPRITES["player"].get_height()) / 2)
    messagex = int((SCREENWIDTH - GAME_SPRITES["message"].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button
            # close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if user press space or up arrow key
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES["background"], (0, 0))
                SCREEN.blit(GAME_SPRITES["player"], (playerx, playery))
                # SCREEN.blit(GAME_SPRITES["message"], (messagex, messagey))        #don't display becuase it's height width are not according to others
                SCREEN.blit(GAME_SPRITES["base"], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENHEIGHT / 2)
    basex = 0
    # Create two pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipe
    upperpipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[0]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[0]["y"]},
    ]
    # list of lower pipe
    lowerpipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[1]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[1]["y"]},
    ]

    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8  # velcoity while flapping
    playerFlapped = False  # only true when our bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS["wing"].play()
        crashTest = isCollide(
            playerx, playery, upperpipes, lowerpipes
        )  # this function will return true if player is crashed
        if crashTest:
            return

        # checks for score
        playerMidPos = playerx + GAME_SPRITES["player"].get_width() / 2
        for pipe in upperpipes:
            pipeMidPos = pipe["x"] + GAME_SPRITES["pipe"][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your score is {score}")
                GAME_SOUNDS["point"].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES["player"].get_height()
        # to change the y co ordinate of bird and stop the birs at bottom
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # Move pipe to left
        for upperpipe, lowerpipe in zip(
            upperpipes, lowerpipes
        ):  # zip make couple of values at respective index
            upperpipe["x"] += pipeVelX
            lowerpipe["x"] += pipeVelX

        # Add a new pipe when the first pipe is about to cross to the left part of screen
        if 0 < upperpipes[0]["x"] < 5:
            newpipe = getRandomPipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])

        # if the pipe is out of screen remove it
        if upperpipes[0]["x"] < -GAME_SPRITES["pipe"][0].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)

        # let's blits our sprites now
        SCREEN.blit(GAME_SPRITES["background"], (0, 0))
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            SCREEN.blit(GAME_SPRITES["pipe"][0], (upperpipe["x"], upperpipe["y"]))
            SCREEN.blit(GAME_SPRITES["pipe"][1], (lowerpipe["x"], lowerpipe["y"]))

        SCREEN.blit(GAME_SPRITES["base"], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES["player"], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES["numbers"][digit].get_width()
        xOffset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES["numbers"][digit], (xOffset, SCREENHEIGHT * 0.12))
            xOffset += GAME_SPRITES["numbers"][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperpipes, lowerpipes):
    if playery > GROUNDY - 25 or playery < 0:
        GAME_SOUNDS["hit"].play()
        return True
    for pipe in upperpipes:
        pipeHeight = GAME_SPRITES["pipe"][0].get_height()
        if (
            playery < pipeHeight + pipe["y"]
            and abs(playerx - pipe["x"]) < GAME_SPRITES["pipe"][0].get_width()
        ):
            GAME_SOUNDS["hit"].play()
            return True
    for pipe in lowerpipes:
        if (
            playery + GAME_SPRITES["player"].get_height() > pipe["y"]
            and abs(playerx - pipe["x"]) < GAME_SPRITES["pipe"][0].get_width()
        ):
            GAME_SOUNDS["hit"].play()
            return True
    return False


def getRandomPipe():
    """
    generates position of two pipes on the screen
    """
    pipeHeight = GAME_SPRITES["pipe"][0].get_height()
    offset = SCREENHEIGHT / 3
    y2 = offset + random.randrange(
        0, int(SCREENHEIGHT - GAME_SPRITES["base"].get_height() - 1.2 * offset)
    )
    pipex = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {"x": pipex, "y": -y1},
        {"x": pipex, "y": y2},
    ]
    return pipe


if __name__ == "__main__":
    pygame.init()  # initilizes all pygame module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("FlappyBird by Abhi")
    GAME_SPRITES["numbers"] = (
        pygame.image.load("gallery/images/0.png").convert_alpha(),
        pygame.image.load("gallery/images/1.png").convert_alpha(),
        pygame.image.load("gallery/images/2.png").convert_alpha(),
        pygame.image.load("gallery/images/3.png").convert_alpha(),
        pygame.image.load("gallery/images/4.png").convert_alpha(),
        pygame.image.load("gallery/images/5.png").convert_alpha(),
        pygame.image.load("gallery/images/6.png").convert_alpha(),
        pygame.image.load("gallery/images/7.png").convert_alpha(),
        pygame.image.load("gallery/images/8.png").convert_alpha(),
        pygame.image.load("gallery/images/9.png").convert_alpha(),
    )
    GAME_SPRITES["message"] = pygame.image.load(
        "gallery/images/message.png"
    ).convert_alpha()
    GAME_SPRITES["base"] = pygame.image.load("gallery/images/base.png").convert_alpha()
    GAME_SPRITES["pipe"] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha(),
    )

    # Game sounds
    GAME_SOUNDS["die"] = pygame.mixer.Sound("gallery/audio/die.wav")
    GAME_SOUNDS["hit"] = pygame.mixer.Sound("gallery/audio/hit.wav")
    GAME_SOUNDS["point"] = pygame.mixer.Sound("gallery/audio/point.wav")
    GAME_SOUNDS["swoosh"] = pygame.mixer.Sound("gallery/audio/swoosh.wav")
    GAME_SOUNDS["wing"] = pygame.mixer.Sound("gallery/audio/wing.wav")

    GAME_SPRITES["background"] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES["player"] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()  # shows welcome screen to user untill he/she press any key
        mainGame()  # this is main game function
