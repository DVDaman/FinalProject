import pygame
from classes import *

room_settings = RoomSettings()
class Map_Engine():
    def __init__(self):
        self.a = "map"
    def load_map(self, file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()
        #Read tile data
        map_data = map_data.split("-") #Splits the tiles at the -'s
        map_size = map_data[len(map_data)-1] #Map dimentions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0])*room_settings.screen_tile
        map_size[1] = int(map_size[1])*room_settings.screen_tile
        tiles = []
        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":")) #Split position from texture
        for tile in tiles:
            tile[0] = tile[0].split(",")
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p) #Convert from text to int
            tiles[tiles.index(tile)] = (pos, tile[1]) #Save to tile list
        #Create terrain as one object
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)
        for tile in tiles:
            if tile[1] in 