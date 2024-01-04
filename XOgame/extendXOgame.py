import pygame
from pygame import mixer
from pygame.locals import *
pygame.init()
#color
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,100)
color_unknown = (150,100,100)

#screen 
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("supersilly")

running = True

#itialize 
markers = []
#player1and2
players = 1
#font
font = pygame.font.Font(None, 40)
line_len = 3

#again rect
img = pygame.image.load("11.jpg")
height_img = img.get_height()
again_rect = pygame.Rect(width // 2 - 120,height // 2 + height_img - 50,250,40)

def draw_grid():
    for i in range(1,12):
        pygame.draw.line(screen,black,(50 * i,0),(50 * i,height),line_len)
        pygame.draw.line(screen,black,(0,50 * i),(width,50 * i),line_len)

def draw_XO():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,green,(50 * x_pos + 5,50 * y_pos + 5),(50 * x_pos + 45,50 * y_pos + 45),line_len)
                pygame.draw.line(screen,green,(50 * x_pos + 45,50 * y_pos + 5),(50 * x_pos + 5,50 * y_pos + 45),line_len)
            if y == -1:
                pygame.draw.circle(screen,red,(50 * x_pos + 25,50 * y_pos + 25),20,line_len)
            y_pos += 1
        x_pos += 1

#checker two cases
clicked = False
game_over = False
winner = 0

def check(x,y):
    if x + 4 < 12:
        if markers[x][y] + markers[x+1][y] + markers[x+2][y] + markers[x+3][y] + markers[x+4][y] == 5:
            return 1
        if markers[x][y] + markers[x+1][y] + markers[x+2][y] + markers[x+3][y] + markers[x+4][y] == -5:  
            return 2
    if y + 4 < 12:
        if markers[x][y] + markers[x][y + 1] + markers[x][y + 2] + markers[x][y + 3] + markers[x][y + 4] == 5:
            return 1
        if markers[x][y] + markers[x][y + 1] + markers[x][y + 2] + markers[x][y + 3] + markers[x][y + 4] == -5:  
            return 2
    if x + 4 < 12 and y + 4 < 12 :
        if markers[x][y] + markers[x + 1][y + 1] + markers[x + 2][y + 2] + markers[x + 3][y + 3] + markers[x + 4][y + 4] == 5:
            return 1
        if markers[x][y] + markers[x + 1][y + 1] + markers[x + 2][y + 2] + markers[x + 3][y + 3] + markers[x + 4][y + 4] == -5:  
            return 2


def check_winner():
    global winner
    global game_over
    for i in range (0,12):
        for j in range(0,12):
            if(check(i,j) == 1):
                winner = 1
                game_over = True 
            elif(check(i,j) == 2):
                winner == 2
                game_over = True 

def kq_winner():
    global winner 
    winner_text = "The sillyone is player" + str(winner)
    winner_text_img = font.render(winner_text,True,color_unknown)
    img_winner = pygame.image.load("11.jpg")
    width_winner = img_winner.get_width()
    height_winner = img_winner.get_height()
    #img_sz = (300,300)
    #img_winner = pygame.transform.scale(img_winner, (width, height))
    screen.blit(img_winner,(width // 2 - 160,height // 2 - 60))
    #draw rect
    #pygame.draw.rect(screen,green,(width // 2 - 100,height // 2,330,50))
    screen.blit(winner_text_img,(width // 2 - 160,height // 2 - 60))
    #draw play again text
    play_again = "want to be a silly ?"
    play_again_font = font.render(play_again,True,color_unknown)
    pygame.draw.rect(screen,blue,again_rect)
    screen.blit(play_again_font,(width // 2 - 120,height // 2 + height_winner - 50))
    
def init_markers():
    global markers 
    for i in range(12):
        row = [0] * 12
        markers.append(row) 
init_markers()

while running :
    #pygame.time.wait(1000)
    screen.fill(white)
    draw_grid()
    check_winner()
    draw_XO()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                 clicked = True 
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[0] // 50
                col = mouse_pos[1] // 50
                if markers[row][col] == 0:
                    markers[row][col] = players
                    players *= -1
                    check_winner()
        if game_over == True:
            #kq_winner()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True 
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                mouse_pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(mouse_pos):
                    markers = []
                    init_markers()
                    game_over = False
                    winner = 0
                    mouse_pos = []
    if game_over == True:
        kq_winner()

    pygame.display.update()
