###################
import pygame, sys, time, os, math
from pygame.locals import *
from classes import Player, PlayerSettings, RoomSettings




def check_keydown_events(p, event, camera_settings, tiles):
    if event.key == K_RIGHT:
        p.moving_right = True
        camera_settings.moving_right = True        
    elif event.key == K_LEFT:
        p.moving_left = True
        camera_settings.moving_left = True
    elif event.key == K_UP:
        p.moving_up = True
        camera_settings.moving_up = True
    elif event.key == K_DOWN:
        p.moving_down = True
        camera_settings.moving_down = True

def check_keyup_events(p, event, camera_settings):
    if event.key == K_RIGHT:
        p.moving_right = False
        camera_settings.moving_right = False
    elif event.key == K_LEFT:
        p.moving_left = False
        camera_settings.moving_left = False
    elif event.key == K_UP:
        p.moving_up = False
        camera_settings.moving_up = False
    elif event.key == K_DOWN:
        p.moving_down = False
        camera_settings.moving_down = False

def check_events(p, camera_settings, tiles):
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            check_keydown_events(p, event, camera_settings, tiles)
        elif event.type == KEYUP:
            check_keyup_events(p, event, camera_settings)

def update_screen(room_settings, screen, p, tiles, camera_settings, terrain):
    screen.blit(tiles.Sky, (0,0))
    screen.blit(terrain, (camera_settings.camerax, camera_settings.cameray))
    p.blitme(room_settings, camera_settings)












#####################################
#Commands transferred over and converted from nes_zelda_map walkthrough
#They dont work :(

# def load_texture(mapData, tileData, room_settings, camera_settings):
#     leftmostTile = camera_settings.camerax // 16
#     topmostTile = camera_settings.cameray // 16
#     roomSurf = pygame.Surface((room_settings.room_width, room_settings.room_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
#     for x in range(0, 11):
#         for y in range(0, 16):
#             roomSurf.blit(tileData[mapData[x][y]], ((x - leftmostTile) * 16, (y - topmostTile) * 16))
#     roomSurf = pygame.transform.scale(roomSurf, (room_settings.screen_width, room_settings.screen_height))
#     return roomSurf

# def loadMapData():

#     # Read in the world map data from the file:
#     fp = open(os.path.join('finalProject\models\map', 'overworldmap.txt'))
#     content = fp.read().strip()
#     fp.close()

#     content = content.split('\n')
#     content = [line.split(' ') for line in content]

#     # invert the xy
#     mapData = [[] for i in range(len(content[0]))]
#     for y in range(len(content)):
#         for x in range(len(content[y])):
#             mapData[x].append(content[y][x])

#     return mapData

# def loadOverworldTiles(room_settings):
#     tilesImg = pygame.image.load(os.path.join('finalProject/models/map','overworldtiles.png'))
#     allOverworldTiles = {}
#     i = 0 # the first tile number is 0
#     for top in range(0, 12*17, 17):
#         for left in range(0, 20*17, 17):
#             tileSurf = pygame.Surface((room_settings.tile_size, room_settings.tile_size), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SRCALPHA)
#             tileSurf.blit(tilesImg, (0,0), (left + 1, top + 1, 16, 16))
#             allOverworldTiles[hex(i)[2:].rjust(2, '0')] = tileSurf
#             i += 1
#     return allOverworldTiles