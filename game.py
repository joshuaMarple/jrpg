import pygame, random, sys
from pygame.locals import *
from button import button
from fight import fight
from globals import *

def start_game():
    global selected_player
    main_clock = pygame.time.Clock()
    window_surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
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
                if event.key == K_SPACE:
                    if fight_menu.hidden == True:
                        fight_menu.show()
                    else:
                        fight_menu.hide()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in players:
                    if i.rect.collidepoint(mouse_pos):
                        selected_player.add(i)
                        i.click()
                        selected_player.empty()
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

    fight_class = fight()
    while True:
        window_surface.fill(BACKGROUNDCOLOR)
        window_surface.blit(background, (0,0))
        event_checker()
        main_clock.tick(FPS)
        all_sprites.update(window_surface)
        pygame.display.update()

start_game()
