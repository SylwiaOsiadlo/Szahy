import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Szahy')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 40)
timer = pygame.time.Clock()
fps = 60

# ame variables i images
white_pieces = ['rook','knight','bishop','king', 'queen','bishop','knight','rook','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
black_pieces = ['rook','knight','bishop','king', 'queen','bishop','knight','rook', 'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
captured_pieces_white = []
captured_pieces_black = []

# 0 - tura biaych nie wybrano 1 - tura biaych wybrano 2 - tura czarnych nie wybrano 3 - tura czarnych wybrano
turn_step = 0
selection = 100
valid_moves = []

#load pieces images
#black pieces
#queen
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen,(80,80))
black_queen_small = pygame.transform.scale(black_queen,(45,45))
#king
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king,(80,80))
black_king_small = pygame.transform.scale(black_king,(45,45))
#rook
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook,(80,80))
black_rook_small = pygame.transform.scale(black_rook,(45,45))
#laufer
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop,(80,80))
black_bishop_small = pygame.transform.scale(black_bishop,(45,45))
#kon
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight,(80,80))
black_knight_small = pygame.transform.scale(black_knight,(45,45))
#pionek
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn,(65,65))
black_pawn_small = pygame.transform.scale(black_pawn,(45,45))
#white pieces
#queen
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen,(80,80))
white_queen_small = pygame.transform.scale(white_queen,(45,45))
#king
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king,(80,80))
white_king_small = pygame.transform.scale(white_king,(45,45))
#rook
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook,(80,80))
white_rook_small = pygame.transform.scale(white_rook,(45,45))
#laufer
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop,(80,80))
white_bishop_small = pygame.transform.scale(white_bishop,(45,45))
#kon
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight,(80,80))
white_knight_small = pygame.transform.scale(white_knight,(45,45))
#pionek
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn,(65,65))
white_pawn_small = pygame.transform.scale(white_pawn,(45,45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, white_knight, white_rook, white_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, white_knight_small, white_rook_small, white_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'rook', 'bishop']

# Kolory różowego dla pól szachownicy
pink_light = (255, 182, 193)  # Jasny różowy
pink_dark = (255, 105, 180)   # Ciemny różowy

#planasza
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, pink_light,[600 -(column * 200), row*100, 100,100])
        else:
            pygame.draw.rect(screen, pink_light,[700 -(column * 200), row*100, 100,100])
        pygame.draw.rect(screen, pink_dark, [0,800,WIDTH,100])
        pygame.draw.rect(screen, 'gold', [0,800,WIDTH,100], 5)
        pygame.draw.rect(screen, 'gold', [800,0,200,HEIGHT], 5)
        status_text = ['Biale: Wybrano bierke','Biale: Prosze wybrac cel', 'Czarne: Wybrano bierke','Czarne: Prosze wybrac cel' ]

        screen.blit(big_font.render(status_text[turn_step], True, 'black'),(20,820))
        for i in range(9):
            pygame.draw.line(screen,'black', (0,100*i), (800,100*i),2)
            pygame.draw.line(screen,'black', (100*i,0), (100*i,800),2)
# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(pink_dark)
    draw_board()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()
