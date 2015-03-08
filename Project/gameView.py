__author__ = 'JoãoGabriel'
import pygame, pygbutton

BLACK = (0, 0, 0)
LIGHTGREY = (160, 160, 160)

class GameView:
    def __init__(self, display, gameModel):
        self.display = display
        self.nextButton = self.createNextButton('NEXT')
        self.gameModel = gameModel

    def createNextButton(self, text):
        return pygbutton.PygButton((1100, 850, 120, 50), text)

    def paintBackground(self):
        pygame.draw.rect(self.display, LIGHTGREY, [0,0,1500,1000], 0)

    def writeScore(self):
        font = pygame.font.Font(None, 30)
        scoreRender = font.render("Score: "+str(self.gameModel.score), True, BLACK)
        self.display.blit(scoreRender, [150, 100])

    def writeStage(self):
        font = pygame.font.Font(None, 30)
        scoreRender = font.render("Stage: "+str(self.gameModel.stage), True, BLACK)
        self.display.blit(scoreRender, [1250, 100])

    def displayNextButton(self):
        self.nextButton.draw(self.display)

    def checkForNextButton(self, event):
        buttonResponse = self.nextButton.handleEvent(event)
        if 'click' in buttonResponse:
            return True

class GameModel:
    def __init__(self):
        self.score = 0
        self.stage = 1
