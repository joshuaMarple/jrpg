import pygame, random, sys
from pygame.locals import *
from button import button
from fight import fight
# from globals import *
import globals

def start_game():
    # global selected_player
    
    main_clock = pygame.time.Clock()
    window_surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    FONT = pygame.font.Font("./res/manteka.ttf", 30)
    globals.GAMESCREEN = window_surface
    window_surface.fill(globals.BACKGROUNDCOLOR)
    globals.BACKGROUND = pygame.transform.scale(pygame.image.load('./res/space.jpg').convert_alpha(), (globals.WINDOWWIDTH, globals.WINDOWHEIGHT))
    
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
                # if event.key == K_SPACE:
                    # if fight_menu.hidden == True:
                        # fight_menu.show()
                    # else:
                        # fight_menu.hide()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in globals.players:
                    if i.rect.collidepoint(mouse_pos):
                        # selected_player.add(i)
                        for j in globals.players:
                            j.unselect()
                        i.click()
                        # for j in globals.buttons:
                        #     print(j)
                        # selected_player.empty()
                for i in globals.buttons:
                    print(i)
                    if i.rect.collidepoint(mouse_pos):
                        i.click()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                for i in globals.buttons:
                    # if i.rect.collidepoint(mouse_pos):
                    i.unclick()
                            
    def draw_text(text, font, surface, x, y):
        textobj = font.render(text, 1, globals.TEXTCOLOR)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    def wait_key():
        draw_text('press enter to unpause', FONT, window_surface, (globals.WINDOWWIDTH /3), (globals.WINDOWHEIGHT / 3))
        draw_text('press esc again to exit', FONT, window_surface, (globals.WINDOWWIDTH /3), (globals.WINDOWHEIGHT / 3) + 50)
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
        window_surface.fill(globals.BACKGROUNDCOLOR)
        window_surface.blit(globals.BACKGROUND, (0,0))
        event_checker()
        main_clock.tick(globals.FPS)
        globals.all_sprites.update(window_surface)
        pygame.display.update()
        for i in globals.popups:
            i.update()

start_game()
