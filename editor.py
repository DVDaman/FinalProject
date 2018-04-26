import pygame, sys, os, time
from pygame.locals import *
from classes import *

room_settings = RoomSettings()
til = Tiles(room_settings)

window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

# txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 100*room_settings.screen_tile, 100*room_settings.screen_tile

selector = pygame.Surface((room_settings.screen_tile, room_settings.screen_tile), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(pygame.Color(0, 0, 255, 100))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = "1"

#Initialize Default Map

for x in range(0, map_width, room_settings.screen_tile):
    for y in range(0, map_height, room_settings.screen_tile):
        tile_data.append([x,y,"1"])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera_move = 1
    window.fill(pygame.Color(100, 30, 40))

    #Draw Map
    for tile in tile_data:
        try:
            window.blit(til.texture_tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass
    pygame.display.update()
    clock.tick(60)
