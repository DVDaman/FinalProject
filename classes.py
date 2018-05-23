###################
import pygame, sys, os, math
from pygame.locals import *


class Player():
    def __init__(self, player_settings, room_settings, screen, camera_settings): 
        #Player images (the 2's are not used because we did not figure out how to animate the player)
        self.down1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_down1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.down2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_down2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.up1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_up1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.up2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_up2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.left1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_left1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.left2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_left2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.right1 = pygame.transform.flip(self.left1, True, False)
        self.right2 = pygame.transform.flip(self.left2, True, False)
        self.image = self.down1
        #Gets rect's
        self.rect =  self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        #location and dimentions of player
        self.height = player_settings.player_height*room_settings.magnification
        self.width = player_settings.player_width*room_settings.magnification
        self.x = ((room_settings.screen_width/2 + self.width/2 - camera_settings.camerax)/room_settings.screen_tile)
        self.y = ((room_settings.screen_height/2 + self.height/2 - camera_settings.cameray)/room_settings.screen_tile)
        self.screen_rect.right = (room_settings.screen_width/2 + self.width/2)
        self.screen_rect.bottom = (room_settings.screen_height/2 - self.height/2)
        self.rect.right = self.screen_rect.right
        self.rect.bottom = self.screen_rect.centery

    def update(self, player_settings):
        #sets the image for the direction of the player
        if self.moving_left:
            # self.rect.centerx -= player_settings.p_speed_factor
            self.image = self.left1
        elif self.moving_right:
            # self.rect.centerx += player_settings.p_speed_factor
            self.image = self.right1
        elif self.moving_down:
            # self.rect.bottom += player_settings.p_speed_factor
            self.image = self.down1
        elif self.moving_up:
            # self.rect.bottom -= player_settings.p_speed_factor
            self.image = self.up1
    def blitme(self, room_settings, camera_settings):
        #blits player and updates position
        self.rect.right = (room_settings.screen_width/2 + self.width/2)
        self.rect.bottom = (room_settings.screen_height/2 + self.height/2)
        self.x = ((room_settings.screen_width/2 + self.width/2 - camera_settings.camerax)/room_settings.screen_tile)
        self.y = ((room_settings.screen_height/2 + self.height/2 - camera_settings.cameray)/room_settings.screen_tile)
        self.screen.blit(self.image, self.rect)
        

class RoomSettings():
    def __init__(self):
        #All the dimentions of things on the screen and the screen
        self.room_width = 256
        self.room_height = 176
        self.magnification = 4
        self.screen_width = int(self.room_width * self.magnification)
        self.screen_height = int(self.room_height * self.magnification)
        self.tile_size = 16
        self.room_tile_width = int(self.room_width / self.tile_size)
        self.room_tile_height = int(self.room_height / self.tile_size)
        self.bg_color = (0,0,0)
        self.screen_tile = int(self.tile_size * self.magnification)
        self.tile_per_roomx = 16
        self.tile_per_roomy = 11
        self.mp = "world.map"

class PlayerSettings():
    def __init__(self, room_settings):
        #Player stats
        self.player_width = 16
        self.player_height = 16
        self.p_speed_factor = room_settings.magnification * 75
        self.p_max_health = 100
        self.p_health = self.p_max_health
        self.p_atk = 5        

class Tiles():
    def __init__(self, room_settings):
        self.x = ["1", "1b", "1p", "1r", "1y", "2", "2b", "2bl", "2br", "2ibl", "2ibr", "2itl", "2itr", "2l", "2pd", "2pl", "2pr", "2pu", "2r", "2t", "2tl", "2tr", "3", "3b", "3bl", "3br", "3c", "3cb", "3cbl", "3cbr", "3cibl", "3cibr", "3citl", "3citr", "3cl", "3cr", "3ct", "3ctl", "3ctr", "3ibl", "3ibr", "3itl", "3itr", "3l", "3r", "3t", "3tl", "3tr", "4", "4bl", "4br", "4t", "4tl", "4tr", "5", "5bl", "5blr", "5br", "5h", "5tbl", "5tbr", "5tl", "5tlr", "5tr", "5v", "5x", "6d", "6h", "6u", "6v", "7", "7bl", "7br", "7t", "7tl", "7tr", "8", "8d", "8l", "8r", "8t", "8tb", "8tbl", "8tbr", "8tl", "8tr", "8w"]
        self.texture_tags = {}
        self.utexture_tags = {}
        for g in self.x:
            self.texture_tags[g] = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map',g+'.png')), (room_settings.screen_tile, room_settings.screen_tile))
            self.utexture_tags[g] = pygame.image.load(os.path.join('finalProject/models/map',g+'.png'))

        #Blocked and speed tiles for each map 
        self.blockeda = []
        self.blockedb = []
        self.speeda = []     
        self.speedb = []   
        
        #Types of tile that are blocked and speed
        self.blocked_types = ["2", "2b", "2bl", "2br", "2l", "2r", "2t", "2tl", "2tr", "3cibl", "3cibr", "3citl", "3citr", "4bl", "4br", "4t", "4tl", "4tr", "4x", "5", "7", "7bl", "7br", "7t", "7tl", "7tr", "8", "8l", "8r"]
        self.speed_types = ["5bl", "5blr", "5br", "5h", "5tbl", "5tbr", "5tl", "5tlr", "5tr", "5v", "5x"]

        #Sky background
        self.sky = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map', 'sky.png')), (room_settings.screen_width, room_settings.screen_height))
        self.Sky = pygame.Surface(self.sky.get_size(), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SRCALPHA)
        self.Sky.blit(self.sky, (0,0))
        del self.sky
        self.size = room_settings.screen_tile
    # def loadtexture(self, file, room_settings):
    #     bitmap = file
    #     surface = pygame.Surface((room_settings.screen_tile, room_settings.screen_tile), pygame.HWSURFACE|pygame.SRCALPHA|pygame.DOUBLEBUF)
    #     surface.blit(bitmap, (0,0))
    #     return surface

    #Checks if tile is blocked or speed
    def blocked_at(self, pos, room_settings):
        if room_settings.mp == "world.map":
            if list(pos) in self.blockeda:
                return True
            else:
                return False
        elif room_settings.mp == "cave.map":
            if list(pos) in self.blockedb:
                return True
            else:
                return False
    def speed_at(self, pos, room_settings):
        if room_settings.mp == "world.map":
            if list(pos) in self.speeda:
                return True
            else:
                return False
        elif room_settings.mp == "cave.map":
            if list(pos) in self.speedb:
                return True
            else:
                return False

class CameraSettings():
    def __init__(self):
        #pos and speed vars
        self.spd = 1
        self.camerax = 0
        self.cameray = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    def update(self, deltatime, room_settings, player_settings, tiles, p):
        #Moves the player based on speed, FPS, blocked tiles, and speed tiles
        if tiles.speed_at((math.floor(p.x-.5), math.floor(p.y-.5)), room_settings):
            self.spd = 1.5
        else:
            self.spd = 1
        if self.moving_left:
            if not tiles.blocked_at((math.floor(p.x-1), math.floor(p.y-.5)), room_settings):
                self.camerax += deltatime * player_settings.p_speed_factor * self.spd
        elif self.moving_right:
            if not tiles.blocked_at((math.floor(p.x), math.floor(p.y-.5)), room_settings):
                self.camerax -= deltatime * player_settings.p_speed_factor * self.spd
        elif self.moving_down:
            if not tiles.blocked_at((math.floor(p.x-.5), math.floor(p.y)), room_settings):
                self.cameray -= deltatime * player_settings.p_speed_factor * self.spd
        elif self.moving_up:
            if not tiles.blocked_at((math.floor(p.x-.5), math.floor(p.y-1)), room_settings):
                self.cameray += deltatime * player_settings.p_speed_factor * self.spd
