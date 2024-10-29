import pygame
import sys
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from pygame.sprite import Group
from pygame.time import Clock
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    clk = Clock()
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)
    pygame.display.set_caption("Alien Invasion!!")

    while True:
        clk.tick(144)
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens,sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb)
            gf.update_aliens(aliens, ai_settings, ship, stats, bullets, screen)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)

run_game()



