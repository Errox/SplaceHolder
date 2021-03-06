#this scripts is a big mixer for all sounds and other musical stuff to all keep it simple and in theme 
import pygame
import sys
import os
import platform
import random

pygame.init()
pygame.mixer.init()

#check if there is already a sound playing. Else fade the current one out

#all music functions
def main_menu():
    pygame.mixer.music.load('resource/soundboard/music/main_menu/main_menu.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def error_music():
    pygame.mixer.music.load('resource/soundboard/music/error/song_1.ogg')
    pygame.mixer.music.play(-1)

def upgrade():
    play = pygame.mixer.Sound('resource/soundboard/upgrade/sound_1.wav')
    play.play()
       
#sequence when game_over scene is triggered
def game_over(score):
    print(score)
    if score == 0:
        pygame.mixer.music.load('resource/soundboard/music/game_over/game_over_0.ogg')
    else:
        #randomizer on death
        random_1 = random.randint(0, 100)
        if random_1 >= 90:
            pygame.mixer.music.load('resource/soundboard/music/game_over/game_over_95.ogg')
        elif random_1 >= 0 and random_1 <= 10:
            pygame.mixer.music.load('resource/soundboard/music/game_over/game_over_85.ogg')
        else:
            pygame.mixer.music.load('resource/soundboard/music/game_over/game_over.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)

#define pause
def pause():
    play = pygame.mixer.Sound('resource/soundboard/menu/in.wav')
    play.play()
    pygame.mixer.music.pause()
#define resume on pause
def resume():
    play = pygame.mixer.Sound('resource/soundboard/menu/out.wav')
    play.play()
    pygame.mixer.music.unpause()

def stranded_main():
    pygame.mixer.music.load('resource/soundboard/music/stranded/song_1.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def invation_main():
    pygame.mixer.music.load('resource/soundboard/music/invation/song_1.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def st_collect():
    stcollect = pygame.mixer.Sound('resource/soundboard/jump/collect.wav')
    stcollect.set_volume(0.5)
    stcollect.play()
    
def st_jump():
    stjump = pygame.mixer.Sound('resource/soundboard/jump/jump.wav')
    stjump.set_volume(0.5)
    stjump.play()

#Astrododge main. 
def ast_main():
    pygame.mixer.music.load('resource/soundboard/music/astrododge/song_1.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_2.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_3.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)
#the hall of fame music during the highscores
def hall_of_fame():
    pygame.mixer.music.load('resource/soundboard/music/hall_of_fame/song_1.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def spst_main():
    pygame.mixer.music.load('resource/soundboard/music/spacestrike/song_1.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_1.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_2.ogg')
    pygame.mixer.music.queue('resource/soundboard/music/astrododge/song_3.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

#sound when shooting a bullet
def bullet_shoot_friendly():
    bullet = pygame.mixer.Sound('resource/soundboard/shoot/friendly/sfx_1.ogg')
    bullet.set_volume(0.3)
    bullet.play()
#sounds when hitting a enemy
def bullet_on_hit_enemy():
    random_1 = random.randint(0, 100)
    if random_1 >= 81:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_1.wav')
    elif random_1 >= 0 and random_1 <= 20:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_2.wav')
    elif random_1 >= 21 and random_1 <= 40:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_3.wav')
    elif random_1 >= 41 and random_1 <= 60:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_4.wav')
    elif random_1 >= 61 and random_1 <= 80:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/enemy/hit_5.wav')
    bullet.set_volume(0.5)
    bullet.play()
#sound when hitting the player
def bullet_on_hit_friendly():
    random_1 = random.randint(0, 60)
    if random_1 >= 41:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/friendly/hit_1.wav')
    elif random_1 >= 0 and random_1 <= 20:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/friendly/hit_2.wav')
    elif random_1 >= 21 and random_1 <= 40:
        bullet = pygame.mixer.Sound('resource/soundboard/onhit/friendly/hit_3.wav')
    bullet.play()

#   SpaceBound sound SpaceSound
def Fight():
    shot = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_wpn_laser6.wav')
    shot.play()

def Powershot():
    Pshot = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_wpn_laser5.wav')
    Pshot.play()

def Healthshot(): 
    Hshot = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_wpn_laser9.wav')
    Hshot.play()

def Hit(): 
    hit = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_deathscream_robot1.wav')
    hit.play()

def Heals():
    heal = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_sound_mechanicalnoise3.wav')
    heal.set_volume(0.5)
    heal.play()

def Death():
    die = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_deathscream_robot2.wav')
    die.play()

def Button():
    Butt = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_menu_move4.wav')
    Butt.play()

def Objective(): 
    obj = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_sound_shutdown1.wav')
    obj.play()

def Walking():
    walk = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_movement_footstepsloop4_slow.wav')
    walk.play()

def Running():
    run = pygame.mixer.Sound('resource/soundboard/SpaceBound/sfx_movement_footstepsloop4_fast.wav')
    run.play()

def Backgroundmusic():
    pygame.mixer.music.load('resource/soundboard/music/SpaceBound/Background_music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

#credits theme
def credits_theme():
    pygame.mixer.music.load('resource/music/credits/song_1.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    

