import pygame
import random
import time

from Define import *

pygame.init()
screen = pygame.display.set_mode((720,640))
running = True
Start = True
times = True
chooses = False
play = False
FONT = pygame.font.SysFont('sans', 20)
FONT_TITLE = pygame.font.SysFont('sans', 50)
FONT_TITLE_2 = pygame.font.SysFont('sans', 35)
TEXT = FONT.render('Click!', TRUE, BLACK)
TEXT_START = FONT_TITLE.render('Start!', TRUE, BLACK)
TEXT_QUIT = FONT_TITLE.render('Quit!', TRUE, BLACK)
TEXT_QUIT_2 = FONT.render('Quit!', TRUE, BLACK)
TEXT_BACK = FONT.render('Back!', TRUE, BLACK)

TEXT_EASY = FONT_TITLE_2.render('EASY :))', TRUE, BLACK)
TEXT_MEDIUM = FONT_TITLE_2.render('MEDIUM :||', TRUE, BLACK)
TEXT_HARD = FONT_TITLE_2.render('HARD :((', TRUE, BLACK)
TEXT_CHOOSES= FONT_TITLE.render("Chooses level!", TRUE, BLACK)
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if Start:
            screen.fill(BG_COLOR)
            pygame.draw.rect(screen, BLACK, (260-5,150-5,200+10,75+10) )
            pygame.draw.rect(screen, WHITE, (260,150,200,75) )
            screen.blit(TEXT_START,  (260+20, 150+5))
            pygame.draw.rect(screen, BLACK, (260-5,415-5,200+10,75+10) )
            pygame.draw.rect(screen, WHITE, (260,415,200,75) )
            screen.blit(TEXT_QUIT,  (260+20, 415+10))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if (260 <= mouse_x <= 260+200 )  and (415 <= mouse_y <= 415+75): 
                        running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if (260 <= mouse_x <= 260+200 )  and (150 <= mouse_y <= 150+75):
                        i=0
                        chooses = True
                        Start = False
                        
        if chooses:
            screen.fill(BG_COLOR)
            pygame.draw.rect(screen, BLACK, (100-5,100-5,520+10,75+10) )
            pygame.draw.rect(screen, WHITE, (100,100,520,75) )
            screen.blit(TEXT_CHOOSES,  (100+20, 100+5))

            pygame.draw.rect(screen, BLACK, (X_EASY-5,Y_LEVEL-5,SIZE_X_LEVEL+10,SIZE_Y_LEVEL+10) )
            pygame.draw.rect(screen, WHITE, (X_EASY,Y_LEVEL,SIZE_X_LEVEL,SIZE_Y_LEVEL) )
            screen.blit(TEXT_EASY,  (X_EASY+20, Y_LEVEL+5))

            pygame.draw.rect(screen, BLACK, (X_MEDIUM-5,Y_LEVEL-5,SIZE_X_LEVEL+10,SIZE_Y_LEVEL+10) )
            pygame.draw.rect(screen, WHITE, (X_MEDIUM,Y_LEVEL,SIZE_X_LEVEL,SIZE_Y_LEVEL) )
            screen.blit(TEXT_MEDIUM,  (X_MEDIUM+20, Y_LEVEL+5))

            pygame.draw.rect(screen, BLACK, (X_HARD-5,Y_LEVEL-5,SIZE_X_LEVEL+10,SIZE_Y_LEVEL+10) )
            pygame.draw.rect(screen, WHITE, (X_HARD,Y_LEVEL,SIZE_X_LEVEL,SIZE_Y_LEVEL) )
            screen.blit(TEXT_HARD,  (X_HARD+20, Y_LEVEL+5))
            pygame.draw.rect(screen, BLACK, (20-5,575-5,50+10,25+10) )
            pygame.draw.rect(screen, WHITE, (20,575,50,25) ) 
            screen.blit(TEXT_QUIT_2,  (20, 575))
            pygame.draw.rect(screen, BLACK, (95-5,575-5,50+10,25+10) )
            pygame.draw.rect(screen, WHITE, (95,575,50,25) ) 
            screen.blit(TEXT_BACK,  (95, 575))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (X_EASY <= mouse_x <= X_EASY+SIZE_X_LEVEL )  and (Y_LEVEL <= mouse_y <= Y_LEVEL + SIZE_Y_LEVEL):
                        R =R_EASY
                        PX=random.randint(0,670)
                        PY=random.randint(0,590)         
                        screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))  
                        pygame.draw.circle(screen, BLACK, (PX, PY), R+5) 
                        pygame.draw.circle(screen, WHITE, (PX, PY), R) 
                        screen.blit(TEXT,  (PX-20, PY-15)) 
                        play = True
                        chooses = False
                    if (X_MEDIUM <= mouse_x <= X_MEDIUM+SIZE_X_LEVEL )  and (Y_LEVEL <= mouse_y <= Y_LEVEL + SIZE_Y_LEVEL):
                        R =R_MEDIUM
                        PX=random.randint(0,670)
                        PY=random.randint(0,590)         
                        screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))  
                        pygame.draw.circle(screen, BLACK, (PX, PY), R+5) 
                        pygame.draw.circle(screen, WHITE, (PX, PY), R) 
                        screen.blit(TEXT,  (PX-20, PY-15))
                        play = True
                        chooses = False
                    if (X_HARD <= mouse_x <= X_HARD+SIZE_X_LEVEL )  and (Y_LEVEL <= mouse_y <= Y_LEVEL + SIZE_Y_LEVEL):
                        R = R_HARD
                        PX=random.randint(0,670)
                        PY=random.randint(0,590)         
                        screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))  
                        pygame.draw.circle(screen, BLACK, (PX, PY), R+5) 
                        pygame.draw.circle(screen, WHITE, (PX, PY), R) 
                        screen.blit(TEXT,  (PX-20, PY-15))
                        play = True
                        chooses = False
                    if (20 <= mouse_x <= 20+50 )  and (575 <= mouse_y <= 615+25):  
                        running = False

                    if (95 <= mouse_x <= 95+50 )  and (575 <= mouse_y <= 615+25): 
                        chooses = False
                        Start =True
        if play:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (PX-R <= mouse_x <= PX+R )  and (PY-R <= mouse_y <= PY+R):                    
                        PX=random.randint(10+R,710-R)
                        PY=random.randint(10+R,580-R)         
                        screen.fill(WHITE)
                        pygame.draw.rect(screen, BLACK, (5,5,710,540) ) 
                        pygame.draw.rect(screen,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), (10,10,700,530) )
                        pygame.draw.circle(screen, BLACK, (PX, PY), R+5) 
                        pygame.draw.circle(screen, WHITE, (PX, PY), R) 
                        screen.blit(TEXT,  (PX-20, PY-15)) 
                        i+=1
                        count= FONT.render("So lan click: "+str(i), TRUE, BLACK)
                        screen.blit(count, (600,600))
                        pygame.draw.rect(screen, BLACK, (20-5,575-5,50+10,25+10) )
                        pygame.draw.rect(screen, WHITE, (20,575,50,25) ) 
                        screen.blit(TEXT_QUIT_2,  (20, 575))
                        pygame.draw.rect(screen, BLACK, (95-5,575-5,50+10,25+10) )
                        pygame.draw.rect(screen, WHITE, (95,575,50,25) ) 
                        screen.blit(TEXT_BACK,  (95, 575))
                    if (20 <= mouse_x <= 20+50 )  and (575 <= mouse_y <= 575+25):  
                        running = False

                    if (95 <= mouse_x <= 95+50 )  and (575 <= mouse_y <= 575+25): 
                        play = False
                        chooses = True
                        



                                  
    pygame.display.flip()
pygame.quit()