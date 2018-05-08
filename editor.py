import pygame, sys, os, time, math
from pygame.locals import *
from classes import *

room_settings = RoomSettings()
til = Tiles(room_settings)


loadmap = input("Load map name: ")
def export_map(file):
    
    map_data = ""
    #Get Map Dimensions
    max_x = 0
    max_y = 0
    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]
    #Save Map Tiles
    for tile1 in tile_data:
        map_data = map_data + str(int(tile1[0]/room_settings.tile_size)) + "," + str(int(tile1[1]/room_settings.tile_size)) + ":" + tile1[2] + "~"
    #Save Map Dimensions
    map_data = map_data + str(int(max_x/room_settings.tile_size)+1) + "," + str(int(max_y/room_settings.tile_size)+1)
    #Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)
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


with open(os.path.join("finalProject/map", (loadmap + ".map")), "r") as map1:
    map1data = map1.read()
map1data = map1data.split("~") #Splits the tiles at the -'s
map1size = map1data[len(map1data)-1] #Map dimentions
map1data.remove(map1size)
map1size = map1size.split(",")
map1size[0] = int(map1size[0])*room_settings.screen_tile
map1size[1] = int(map1size[1])*room_settings.screen_tile
tiles = []
for tile in range(len(map1data)):
    map1data[tile] = map1data[tile].replace("\n", "")
    tiles.append(map1data[tile].split(":")) #Split position from texture
for tile in tiles:
    tile[0] = tile[0].split(",")
    pos = tile[0]
    for p in pos:
        pos[pos.index(p)] = int(p) #Convert from text to int
    tiles[tiles.index(tile)] = (pos, tile[1]) #Save to tile list
#Create terrain as one object
for tile in tiles:
    xy = tile[0]
    if tile[1] in til.texture_tags:
        tile_data.append([xy[0]*room_settings.tile_size, xy[1]*room_settings.tile_size, tile[1]])

# for x in range(0, map_width, room_settings.tile_size):
#     for y in range(0, map_height, room_settings.tile_size):
#         tile_data.append([x,y,"1"])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                camera_move = 1
            elif event.key == pygame.K_DOWN:
                camera_move = 2
            elif event.key == pygame.K_LEFT:
                camera_move = 3
            elif event.key == pygame.K_RIGHT:
                camera_move = 4
            #Saving
            if event.key == pygame.K_RETURN:
                filename = input("File name: ")
                export_map(os.path.join("finalProject/map", (filename + ".map")))
                print("Success")
            #Brushes
            if event.key == pygame.K_BACKSPACE:
                brush = "remove"
            if event.key == pygame.K_1:
                brush = "1"                
            if event.key == pygame.K_2:
                brush = "2"
            if event.key == pygame.K_3:
                brush = "3"
            if event.key == pygame.K_4:
                brush = "4"
            if event.key == pygame.K_5:
                brush = "5"
            if event.key == pygame.K_6:
                brush = "6"
            if event.key == pygame.K_7:
                brush = "7"
            if event.key == pygame.K_8:
                brush = "8"
            if event.key == pygame.K_t:
                brush = brush + "t"
            if event.key == pygame.K_r:
                brush = brush + "r"
            if event.key == pygame.K_b:
                brush = brush + "b"
            if event.key == pygame.K_l:
                brush = brush + "l"
            if event.key == pygame.K_i:
                brush = brush + "i"
            if event.key == pygame.K_h:
                brush = brush + "h"
            if event.key == pygame.K_v:
                brush = brush + "v"
            if event.key == pygame.K_y:
                brush = brush + "y"
            if event.key == pygame.K_p:
                brush = brush + "p"
            if event.key == pygame.K_x:
                brush = brush + "x"
            if event.key == pygame.K_u:
                brush = brush + "u"
            if event.key == pygame.K_d:
                brush = brush + "d"
        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0]/room_settings.tile_size)*room_settings.tile_size
            mouse_y = math.floor(mouse_pos[1]/room_settings.tile_size)*room_settings.tile_size
        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush] #List boi
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break
            if not found:
                if not brush == "remove":
                    tile_data.append(tile)
            else:
                if brush == "remove":
                    #Remove tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Gone")
                else:
                    print("No thanks.")
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
    window.fill(pygame.Color(100, 30, 80))

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
