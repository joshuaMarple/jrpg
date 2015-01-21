import pygame, random, sys
from pygame.locals import *
from button import button

WINDOWWIDTH = 0
WINDOWHEIGHT = 0
    
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60
    
FONT = 0

TEXTCOLOR = (0,0,0)

# def remove():
    # for i in buttons:
        # i.kill()

buttons = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

def printer():
    print("test")

def test():
    global WINDOWWIDTH
    global WINDOWHEIGHT
    print(WINDOWHEIGHT)
    print(WINDOWWIDTH)
    buttonA = button(WINDOWWIDTH/2, WINDOWHEIGHT/2, WINDOWWIDTH/2, WINDOWHEIGHT/2, "test2", lambda : (), True)
    # buttonA.rect.x = 200
    # buttonA.rect.y = 200
    buttons.add(buttonA)
    all_sprites.add(buttonA)
    

def start_game():
    global WINDOWWIDTH
    global WINDOWHEIGHT
    pygame.init()
    main_clock = pygame.time.Clock()

    window_surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    WINDOWWIDTH = pygame.display.Info().current_w
    WINDOWHEIGHT = pygame.display.Info().current_h

    FONT = pygame.font.Font("./res/manteka.ttf", 30)
    
    window_surface.fill(BACKGROUNDCOLOR)

    background = pygame.transform.scale(pygame.image.load('./res/space.jpg').convert_alpha(), (WINDOWWIDTH, WINDOWHEIGHT))
    
    def terminate():
        pygame.quit()
        sys.exit()


    def event_checker():
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    wait_key()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in buttons:
                    if i.rect.collidepoint(mouse_pos):
                        i.click()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for i in buttons:
                    if i.rect.collidepoint(mouse_pos):
                        i.unclick()
                            
    def draw_text(text, font, surface, x, y):
        textobj = font.render(text, 1, TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    def wait_key():
        draw_text('press enter to unpause', FONT, window_surface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3))
        draw_text('press esc again to exit', FONT, window_surface, (WINDOWWIDTH /3), (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminate()
                    if event.key == K_RETURN:
                        return
               
                    


    buttonA = button(0, WINDOWHEIGHT*2/3, WINDOWWIDTH/3, WINDOWHEIGHT/3, "test", test, False)
    # buttonA.rect.x = random.randrange(WINDOWWIDTH)
    # buttonA.rect.y = random.randrange(WINDOWHEIGHT)
    buttons.add(buttonA)
    all_sprites.add(buttonA)
    while True:
        window_surface.fill(BACKGROUNDCOLOR)
        window_surface.blit(background, (0,0))

        
        # for event in pygame.event.get():
        event_checker()
        main_clock.tick(FPS)
        all_sprites.update(window_surface)
        # all_sprites.draw(window_surface)
        pygame.display.update()
        # wait_key()

start_game()


