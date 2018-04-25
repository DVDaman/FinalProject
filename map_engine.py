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