import pygame
import classes

class Map_Engine():
    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()