import pygame, sys, math
from classes import *
from map_engine import *

room_settings = RoomSettings()
tiles = Tiles(room_settings)

def export_map(file):
    map_data = ""

    # Get Map Dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / tiles.size)) + "," + str(int(tile[1] / tiles.size)) + ":" + tile[2] + "-"
        

    # Save Map Dimensions
    map_data = map_data + str(int(max_x / tiles.size)) + "," + str(int(max_y / tiles.size))


    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)



window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()


# txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_width, map_height = 10 * tiles.size, 10 * tiles.size


selector = pygame.Surface((tiles.size, tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(pygame.Color(0,0,255,100))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0


brush = "1"

# map_engine = Map_Engine()
# terrain = map_engine.load_map(os.path.join("finalProject/map", "world.map"))


# with open(os.path.join("finalProject/map", "world.map"), "r") as mapfile:
#     map_data = mapfile.read()
# #Read tile data
# map_data = map_data.split("-") #Splits the tiles at the -'s
# map_size = map_data[len(map_data)-1] #Map dimentions
# map_data.remove(map_size)
# map_size = map_size.split(",")
# map_size[0] = int(map_size[0])*room_settings.screen_tile
# map_size[1] = int(map_size[1])*room_settings.screen_tile
# tile_data = []
# for tile in range(len(map_data)):
#     map_data[tile] = map_data[tile].replace("\n", "")
#     tile_data.append(map_data[tile].split(":")) #Split position from texture
# for tile in tile_data:
#     ggg = tile[0]
#     tile[0] = tile[0].split(",")
#     pos = tile[0]
#     for p in pos:
#         pos[pos.index(p)] = int(p) #Convert from text to int
#     tile_data[tile_data.index(tile)] = (pos, tile[1]) #Save to tile list


# Initialize Default Map

# for x in range(0, map_width, tiles.size):
#     for y in range(0, map_height, tiles.size):
#         tile_data.append([x, y, "1"])




isRunning = True


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            if event.key == pygame.K_BACKSPACE:
                brush = "r"
            elif event.key == pygame.K_F1:
                selection = input("Brush Tag: ")
                brush = selection
            elif event.key == pygame.K_1:
                brush = "1"
            elif event.key == pygame.K_2:
                brush = "2"
            elif event.key == pygame.K_3:
                brush = "3"
            elif event.key == pygame.K_4:
                brush = "4"
            elif event.key == pygame.K_5:
                brush = "5"
            elif event.key == pygame.K_6:
                brush = "6"
            elif event.key == pygame.K_7:
                brush = "7"
            elif event.key == pygame.K_i:
                brush = brush + "i"
            elif event.key == pygame.K_t:
                brush = brush + "t"
            elif event.key == pygame.K_b:
                brush = brush + "b"
            elif event.key == pygame.K_r:
                brush = brush + "r"
            elif event.key == pygame.K_l:
                brush = brush + "l"
            elif event.key == pygame.K_h:
                brush = brush + "h"
            elif event.key == pygame.K_v:
                brush = brush + "v"

            # SAVE MAP
            if event.key == pygame.K_F11:
                name = input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully!")
            

        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / tiles.size) * tiles.size
            mouse_y = math.floor(mouse_pos[1] / tiles.size) * tiles.size

        if event.type == pygame.MOUSEBUTTONDOWN:
            tile = [mouse_x - camera_x, mouse_y - camera_y, brush]   # Keep this as a list

            # Is a tile already placed here?
            found = False
            for t in tile_data:
                if t[0] == tile[0] and t[1] == tile[1]:
                    found = True
                    break

            # If this tile space is empty
            if not found:
                if not brush == "r":
                    tile_data.append(tile)

            # If this tile space is not empty
            else:
                # Are we using the rubber tool?
                if brush == "r":
                    # Remove Tile
                    for t in tile_data:
                        if t[0] == tile[0] and t[1] == tile[1]:
                            tile_data.remove(t)
                            print("Tile Removed!")

                else:
                    # Sorry! A tile is already placed here!
                    print("A tile is already placed here!")
                            



    # LOGIC
    if camera_move == 1:
        camera_y += tiles.size
    elif camera_move == 2:
        camera_y -= tiles.size
    elif camera_move == 3:
        camera_x += tiles.size
    elif camera_move == 4:
        camera_x -= tiles.size



    # RENDER GRAPHICS


    window.fill(pygame.Color(0,50,0,100))

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(tiles.texture_tags[tile[2]], (tile[0]+camera_x, tile[1]+camera_y))
        except:
            pass


    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))
    
    

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()