import pygame
import random
import os

HEIGHT, WIDTH = 800, 500
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pong")
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fps = 60

scoreFont = pygame.font.Font('assets/arcadeclassic.ttf', 32)
winFont = pygame.font.Font('assets/arcadeclassic.ttf', 40)


bounce = pygame.mixer.Sound(os.path.join('assets', 'bounce.wav'))
point = pygame.mixer.Sound(os.path.join('assets', 'point.wav'))
win = pygame.mixer.Sound(os.path.join('assets', 'win.wav'))

def displayGame(paddle1, paddle2, ballX, ballY, score):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, pygame.Rect(105, paddle1, 5, 75))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(685, paddle2, 5, 75))
    pygame.draw.circle(WIN, WHITE, (ballX, ballY), 7)

    #pygame.draw.rect(WIN, WHITE, pygame.Rect(399, 0, 2, 75))

    score0 = scoreFont.render(chr(score[0] + 48), True, WHITE)
    WIN.blit(score0, (10, 10))
    score1 = scoreFont.render(chr(score[1] + 48), True, WHITE)
    WIN.blit(score1, (773, 10))
    pygame.display.update()
    


def main():
    paddle1 = 225
    paddle2 = 225
    ballX = 400
    ballY = 250
    score = [0, 0]
    run = True
    waitingScreen = True
    clock = pygame.time.Clock()
    while run:

        if score[0] == 7:
            winMessage = winFont.render('Player   1   Wins!', True, WHITE)
            winMessageRect = winMessage.get_rect()
            winMessageRect.center = (HEIGHT // 2, WIDTH // 2)
            pygame.mixer.Sound.play(win)
            for i in range(4):
                WIN.blit(winMessage, winMessageRect)
                pygame.display.update()
                pygame.time.wait(500)
                if i < 3:
                    displayGame(paddle1, paddle2, ballX, ballY, score)
                    pygame.time.wait(500)
            pygame.quit()
            run = False
            break
        elif score[1] == 7:
            winMessage = winFont.render('Player   2   Wins!', True, WHITE)
            winMessageRect = winMessage.get_rect()
            winMessageRect.center = (HEIGHT // 2, WIDTH // 2)
            pygame.mixer.Sound.play(win)
            for i in range(4):
                WIN.blit(winMessage, winMessageRect)
                pygame.display.update()
                pygame.time.wait(500)
                if i < 3:
                    displayGame(paddle1, paddle2, ballX, ballY, score)
                    pygame.time.wait(500)
            pygame.quit()
            run = False
            break

        fps = 60

        ballXVelocity = random.uniform(4, 7)
        ballYVelocity = random.uniform(3, 8)
        if score[0] == score[1]:
            if random.randint(0, 1) == 0:
                ballXVelocity = -ballXVelocity
        elif score[0] > score[1]:
            ballXVelocity = -ballXVelocity
        if random.randint(0, 1) == 0:
            ballYVelocity = -ballYVelocity

        paddle1 = 225
        paddle2 = 225
        ballX = 400
        ballY = 250
        
        if waitingScreen == True:
            waitingText1 = winFont.render('Press   Space   To   Begin', True, WHITE)
            waitingTextRect1 = waitingText1.get_rect()
            waitingTextRect1.center = (HEIGHT // 2, WIDTH // 2)
            WIN.blit(waitingText1, waitingTextRect1)
            pygame.display.update()
        else:
            displayGame(paddle1, paddle2, ballX, ballY, score)
        pygame.time.wait(500)

        roundOver = False
        while roundOver == False:

            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waitingScreen = False
            
            if waitingScreen == True:
                continue

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] == 1:
                if paddle1 > 7:
                    paddle1 -= 7
                else:
                    paddle1 = 0
            if keys[pygame.K_s] == 1:
                if paddle1 < 418:
                    paddle1 += 7
                else:
                    paddle1 = 425
            if keys[pygame.K_UP] == 1:
                if paddle2 > 7:
                    paddle2 -= 7
                else:
                    paddle2 = 0
            if keys[pygame.K_DOWN] == 1:
                if paddle2 < 418:
                    paddle2 += 7
                else:
                    paddle2 = 425

            ballY += ballYVelocity
            if ballY > 493:
                ballY -= (2 * (ballY - 493))
                ballYVelocity = -ballYVelocity
                pygame.mixer.Sound.play(bounce)
            elif ballY < 7:
                ballY += (2 * (7 - ballY))
                ballYVelocity = -ballYVelocity
                pygame.mixer.Sound.play(bounce)
            
            ballX += ballXVelocity

            if 110 <= ballX < 117:
                if paddle1 <= ballY <= (paddle1 + 75):
                    ballX += (2 * (117 - ballX))
                    ballXVelocity = -ballXVelocity
                    pygame.mixer.Sound.play(bounce)

            if 683 < ballX <= 690:
                if paddle2 <= ballY <= (paddle2 + 75):
                    ballX -= (2 * (ballX - 683))
                    ballXVelocity = -ballXVelocity
                    pygame.mixer.Sound.play(bounce)

            if ballX < 7:
                ballX = 7
                roundOver = True
                score[1] += 1
                pygame.mixer.Sound.play(point)
            elif ballX > 793:
                ballX = 793
                roundOver = True
                score[0] += 1
                pygame.mixer.Sound.play(point)
 
            fps += .1

            displayGame(paddle1, paddle2, ballX, ballY, score)
    

    pygame.quit()
    



if __name__ == "__main__":
    main()