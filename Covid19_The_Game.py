import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from scientist import Scientist

import events as gf

from coronavirus import Covid_19

# the function is supposed to initialize the game, create a screen object and watch for the events

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # uses a tuple to set the dimensions

    pygame.display.set_caption("Covid19 The Game")

    #creating the scientist

    scientist=Scientist(ai_settings,screen)
    viruses=Group()
    cure=Group()
    gf.create_fleet(ai_settings,screen,scientist,viruses)
    # main loop for the game

    while True:

        # watching for the events
        gf.check_events(ai_settings,screen,scientist,cure)
        scientist.update()
        #getting rid of cures that have disappeared

        gf.update_cure(cure)
        gf.update_viruses(ai_settings,viruses)
        # Drawn the mostly recent screen

        gf.update_screen(ai_settings,screen,scientist,viruses,cure)




run_game()

