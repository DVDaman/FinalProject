"""
Many concepts and functions were inspired by Meloonatic Melons on Youtube but
all needed to be adapted and modified to fit into this code. The player texures
are from nesZeldaWalkingTour by Al Sweigart and the terrain texture are 
inspired by the nesZeldaWalkingTour but have been modified and new ones have 
been added.
"""
##############################################Daniele and Curran###############################################

import pygame, random, sys, os, time
from pygame.locals import *
from classes import *
import game_functions as gf
from pygame.sprite import Group
from map_engine import *

pygame.init()


clock = pygame.time.Clock()

def setup():
    #Creates all the variables and calls all the classes
    global room_settings, screen, bg_color, p, player_settings, countSec, countFrame, FPS, fps_font, tiles, camera_settings, deltatime, terraina, map_engine, terrainb
    room_settings = RoomSettings()
    player_settings = PlayerSettings(room_settings)
    camera_settings = CameraSettings()
    map_engine = Map_Engine()
    screen = pygame.display.set_mode((room_settings.screen_width, room_settings.screen_height), pygame.HWSURFACE|pygame.SRCALPHA|pygame.DOUBLEBUF)
    pygame.display.set_caption("r/GantMemes")
    bg_color = room_settings.bg_color
    p = Player(player_settings, room_settings, screen, camera_settings)
    countSec = 0
    countFrame = 0
    FPS = 0
    deltatime = 0
    fps_font = pygame.font.Font("C://Windows//Fonts//PrestigeEliteStd-Bd.otf", (room_settings.magnification*10))
    tiles = Tiles(room_settings)
    terraina = map_engine.load_map(os.path.join("finalProject/map", "world.map"), tiles)
    terrainb = map_engine.load_map(os.path.join("finalProject/map", "cave.map"), tiles)

def show_fps():
    #Renders FPS on screen
    fps_overlay = fps_font.render("FPS: "+str(FPS), True, (0, 255, 0, 100))
    screen.blit(fps_overlay, (0,0))

def count_fps():
    #Counts how many times the game loop runs each second
    global countFrame, countSec, FPS, deltatime
    if countSec == time.strftime("%S"):
        countFrame += 1
    else:
        FPS = countFrame
        countFrame = 0
        countSec = time.strftime("%S")
        if FPS > 0:
            #To set the same player speed for all FPS if stable
            deltatime = 1 / FPS

setup()
while True:
    
    # Checks events
    gf.check_events(p, camera_settings, tiles) 
    p.update(player_settings)
    camera_settings.update(deltatime, room_settings, player_settings, tiles, p)
    

    #Blits everything
    gf.update_screen(room_settings, screen, p, tiles, camera_settings, terraina, map_engine, terrainb)

    show_fps()
    #Reloads the screen
    pygame.display.update()
    count_fps()
    clock.tick(100)