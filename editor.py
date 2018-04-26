import pygame, sys, os, time, math
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

map_width, map_height = 10*room_settings.tile_size, 10*room_settings.tile_size

selector = pygame.Surface((room_settings.tile_size, room_settings.tile_size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(pygame.Color(0, 0, 255, 100))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = "1"

#Initialize Default Map

for x in range(0, map_width, room_settings.tile_size):
    for y in range(0, map_height, room_settings.tile_size):
        tile_data.append([x,y,"1"])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4
        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0]/room_settings.tile_size)*room_settings.tile_size
            mouse_y = math.floor(mouse_pos[1]/room_settings.tile_size)*room_settings.tile_size
    #Logic
    if camera_move == 1:
        camera_y += room_settings.tile_size
    elif camera_move == 2:
        camera_y -= room_settings.tile_size
    elif camera_move == 3:
        camera_x += room_settings.tile_size
    elif camera_move == 4:
        camera_x -= room_settings.tile_size

    #Render Graphics
    window.fill(pygame.Color(100, 30, 40))

    #Draw Map
    for tile in tile_data:
        try:
            window.blit(til.utexture_tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    #Draw selector
    window.blit(selector, (mouse_x, mouse_y))
    pygame.display.update()
    clock.tick(60)
