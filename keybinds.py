def start(score):
    #defining every library needed
    import sys
    import pygame
    import os
    import menu
    import soundboard
    import astrodoge 
    import spacestrike
    import SpaceBound
    import Stranded
    import sumo_smash
    from time import sleep

    #setting variables
    FPS     = 30
    X       = 500
    Y       = 100
    WHITE   = (255, 255, 255)
    BLACK   = (0, 0, 0)

    #setting the settings of pygame itself
    screen = pygame.display.set_mode((900,900))
    pygame.display.set_caption("game_over")
    font = pygame.font.SysFont('resource/fonts/Arcadepix.ttf', 40)
    clock = pygame.time.Clock()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (X,Y)
    define_location = "main_menu"
        
    #initializing pygame's mixer
    # pygame.mixer.init()
    # pygame.mixer.music.load("resource/music/main_menu/main_menu.ogg")
    # pygame.mixer.music.play(-1)

    #initiate a image loader
    def load_image(name):
        image = pygame.image.load(name)
        return image
    
    #start the main menu board.
    def start_game_over():
        #set background
        background = pygame.image.load('resource/images/game_over/game_overbg.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        buttons_game_over()

    def buttons_game_over():
        quit_button         = pygame.image.load('resource/images/game_over/button_quit.png').convert()
        quit_rect           = quit_button.get_rect()
        screen.blit(quit_button, (325,550))
    
    def text_score():        
        scoretext = font.render("Your Score was : {0}".format(score), 1, WHITE)
        screen.blit(scoretext, (300, 400))

    #beginning of the main loop
    main_loop = True
    my_sprite = animated_select_planet()
    my_group = pygame.sprite.Group(my_sprite)
    soundboard.game_over(score)
    while main_loop:
        #reset the screen and set screen image's
        screen.fill(BLACK)
        clock.tick(FPS)
        start_game_over()
        my_group.update()
        my_group.draw(screen)
        text_score()
        #check events
        for evento in pygame.event.get():
            #define event's of quiting the game.
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            #printing every event that's happening within the python script.
            print(evento)
            #Catch mouse position and if it's pressed on the button
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 315 and pygame.mouse.get_pos()[1] >= 550:
                    if pygame.mouse.get_pos()[0] <= 593 and pygame.mouse.get_pos()[1] <= 615:
                        menu.start_menu()


        pygame.display.flip()

    pygame.quit()
    quit()