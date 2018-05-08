###################
import pygame, sys, os, math
from pygame.locals import *


class Player():
    def __init__(self, player_settings, room_settings, screen, camera_settings): 
        self.down1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_down1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.down2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_down2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.up1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_up1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.up2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_up2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.left1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_left1.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.left2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/player','player_left2.png')), (player_settings.player_width*room_settings.magnification, player_settings.player_width*room_settings.magnification))
        self.right1 = pygame.transform.flip(self.left1, True, False)
        self.right2 = pygame.transform.flip(self.left2, True, False)
        self.image = self.down1
        self.rect =  self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.height = player_settings.player_height*room_settings.magnification
        self.width = player_settings.player_width*room_settings.magnification
        self.x = ((room_settings.screen_width/2 + self.width/2 - camera_settings.camerax)/room_settings.screen_tile)
        self.y = ((room_settings.screen_height/2 + self.height/2 - camera_settings.cameray)/room_settings.screen_tile)
        self.screen_rect.right = (room_settings.screen_width/2 + self.width/2)
        self.screen_rect.bottom = (room_settings.screen_height/2 - self.height/2)
        self.rect.right = self.screen_rect.right
        self.rect.bottom = self.screen_rect.centery


    def update(self, player_settings):
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
        self.rect.right = (room_settings.screen_width/2 + self.width/2)
        self.rect.bottom = (room_settings.screen_height/2 + self.height/2)
        self.x = ((room_settings.screen_width/2 + self.width/2 - camera_settings.camerax)/room_settings.screen_tile)
        self.y = ((room_settings.screen_height/2 + self.height/2 - camera_settings.cameray)/room_settings.screen_tile)
        self.screen.blit(self.image, self.rect)
        

class RoomSettings():
    def __init__(self):
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

class PlayerSettings():
    def __init__(self, room_settings):
        self.player_width = 16
        self.player_height = 16
        self.p_speed_factor = room_settings.magnification * 75
        self.p_max_health = 100
        self.p_health = self.p_max_health
        self.p_atk = 5        

class Tiles():
    def __init__(self, room_settings):

        self.blocked = []
        self.blocked_types = ["2", "2b", "2bl", "2br", "2l", "2r", "2t", "2tl", "2tr", "4bl", "4br", "4t", "4tl", "4tr", "5", "7", "7bl", "7br", "7t", "7tl", "7tr", "8", "8l", "8r"]

        self.speed = []
        self.speed_types = ["5bl", "5blr", "5br", "5h", "5tbl", "5tbr", "5tl", "5tlr", "5tr", "5v", "5x"]

        ################
        self.t1 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','1.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t1b = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','1b.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t1p = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','1p.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t1r = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','1r.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t1y = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','1y.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2b = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2b.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2ibl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2ibl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2ibr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2ibr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2itl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2itl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2itr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2itr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2l = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2l.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2pd = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2pd.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2pl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2pl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2pr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2pr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2pu = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2pu.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2r = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2r.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t2tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','2tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3b = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3b.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3ibl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3ibl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3ibr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3ibr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3itl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3itl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3itr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3itr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3l = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3l.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3r = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3r.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t3tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','3tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t4tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','4tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5blr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5blr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5h = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5h.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5tbl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5tbl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5tbr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5tbr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5tlr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5tlr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5v = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5v.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t5x = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','5x.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t6h = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','6h.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t6t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','6t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t6v = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','6v.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7bl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7bl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7br = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7br.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7t = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7t.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7tl = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7tl.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t7tr = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','7tr.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t8 = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','8.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t8d = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','8d.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t8l = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','8l.png')), (room_settings.screen_tile, room_settings.screen_tile))
        self.t8r = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map','8r.png')), (room_settings.screen_tile, room_settings.screen_tile))
        ###################
        self.u1 = pygame.image.load(os.path.join('finalProject/models/map','1.png'))
        self.u1b = pygame.image.load(os.path.join('finalProject/models/map','1b.png'))
        self.u1p = pygame.image.load(os.path.join('finalProject/models/map','1p.png'))
        self.u1r = pygame.image.load(os.path.join('finalProject/models/map','1r.png'))
        self.u1y = pygame.image.load(os.path.join('finalProject/models/map','1y.png'))
        self.u2 = pygame.image.load(os.path.join('finalProject/models/map','2.png'))
        self.u2b = pygame.image.load(os.path.join('finalProject/models/map','2b.png'))
        self.u2bl = pygame.image.load(os.path.join('finalProject/models/map','2bl.png'))
        self.u2br = pygame.image.load(os.path.join('finalProject/models/map','2br.png'))
        self.u2ibl = pygame.image.load(os.path.join('finalProject/models/map','2ibl.png'))
        self.u2ibr = pygame.image.load(os.path.join('finalProject/models/map','2ibr.png'))
        self.u2itl = pygame.image.load(os.path.join('finalProject/models/map','2itl.png'))
        self.u2itr = pygame.image.load(os.path.join('finalProject/models/map','2itr.png'))
        self.u2l = pygame.image.load(os.path.join('finalProject/models/map','2l.png'))
        self.u2pd = pygame.image.load(os.path.join('finalProject/models/map','2pd.png'))
        self.u2pl = pygame.image.load(os.path.join('finalProject/models/map','2pl.png'))
        self.u2pr = pygame.image.load(os.path.join('finalProject/models/map','2pr.png'))
        self.u2pu = pygame.image.load(os.path.join('finalProject/models/map','2pu.png'))
        self.u2r = pygame.image.load(os.path.join('finalProject/models/map','2r.png'))
        self.u2t = pygame.image.load(os.path.join('finalProject/models/map','2t.png'))
        self.u2tl = pygame.image.load(os.path.join('finalProject/models/map','2tl.png'))
        self.u2tr = pygame.image.load(os.path.join('finalProject/models/map','2tr.png'))
        self.u3 = pygame.image.load(os.path.join('finalProject/models/map','3.png'))
        self.u3b = pygame.image.load(os.path.join('finalProject/models/map','3b.png'))
        self.u3bl = pygame.image.load(os.path.join('finalProject/models/map','3bl.png'))
        self.u3br = pygame.image.load(os.path.join('finalProject/models/map','3br.png'))
        self.u3ibl = pygame.image.load(os.path.join('finalProject/models/map','3ibl.png'))
        self.u3ibr = pygame.image.load(os.path.join('finalProject/models/map','3ibr.png'))
        self.u3itl = pygame.image.load(os.path.join('finalProject/models/map','3itl.png'))
        self.u3itr = pygame.image.load(os.path.join('finalProject/models/map','3itr.png'))
        self.u3l = pygame.image.load(os.path.join('finalProject/models/map','3l.png'))
        self.u3r = pygame.image.load(os.path.join('finalProject/models/map','3r.png'))
        self.u3t = pygame.image.load(os.path.join('finalProject/models/map','3t.png'))
        self.u3tl = pygame.image.load(os.path.join('finalProject/models/map','3tl.png'))
        self.u3tr = pygame.image.load(os.path.join('finalProject/models/map','3tr.png'))
        self.u4 = pygame.image.load(os.path.join('finalProject/models/map','4.png'))
        self.u4bl = pygame.image.load(os.path.join('finalProject/models/map','4bl.png'))
        self.u4br = pygame.image.load(os.path.join('finalProject/models/map','4br.png'))
        self.u4t = pygame.image.load(os.path.join('finalProject/models/map','4t.png'))
        self.u4tl = pygame.image.load(os.path.join('finalProject/models/map','4tl.png'))
        self.u4tr = pygame.image.load(os.path.join('finalProject/models/map','4tr.png'))
        self.u5 = pygame.image.load(os.path.join('finalProject/models/map','5.png'))
        self.u5bl = pygame.image.load(os.path.join('finalProject/models/map','5bl.png'))
        self.u5blr = pygame.image.load(os.path.join('finalProject/models/map','5blr.png'))
        self.u5br = pygame.image.load(os.path.join('finalProject/models/map','5br.png'))
        self.u5h = pygame.image.load(os.path.join('finalProject/models/map','5h.png'))
        self.u5tbl = pygame.image.load(os.path.join('finalProject/models/map','5tbl.png'))
        self.u5tbr = pygame.image.load(os.path.join('finalProject/models/map','5tbr.png'))
        self.u5tl = pygame.image.load(os.path.join('finalProject/models/map','5tl.png'))
        self.u5tlr = pygame.image.load(os.path.join('finalProject/models/map','5tlr.png'))
        self.u5tr = pygame.image.load(os.path.join('finalProject/models/map','5tr.png'))
        self.u5v = pygame.image.load(os.path.join('finalProject/models/map','5v.png'))
        self.u5x = pygame.image.load(os.path.join('finalProject/models/map','5x.png'))
        self.u6h = pygame.image.load(os.path.join('finalProject/models/map','6h.png'))
        self.u6t = pygame.image.load(os.path.join('finalProject/models/map','6t.png'))
        self.u6v = pygame.image.load(os.path.join('finalProject/models/map','6v.png'))
        self.u7 = pygame.image.load(os.path.join('finalProject/models/map','7.png'))
        self.u7bl = pygame.image.load(os.path.join('finalProject/models/map','7bl.png'))
        self.u7br = pygame.image.load(os.path.join('finalProject/models/map','7br.png'))
        self.u7t = pygame.image.load(os.path.join('finalProject/models/map','7t.png'))
        self.u7tl = pygame.image.load(os.path.join('finalProject/models/map','7tl.png'))
        self.u7tr = pygame.image.load(os.path.join('finalProject/models/map','7tr.png'))
        self.u8 = pygame.image.load(os.path.join('finalProject/models/map','8.png'))
        self.u8d = pygame.image.load(os.path.join('finalProject/models/map','8d.png'))
        self.u8l = pygame.image.load(os.path.join('finalProject/models/map','8l.png'))
        self.u8r = pygame.image.load(os.path.join('finalProject/models/map','8r.png'))
        ###############
        self.texture_tags = {"1":self.t1, "1b":self.t1b, "1p":self.t1p, "1r":self.t1r, "1y":self.t1y, "2":self.t2, "2b":self.t2b, "2bl":self.t2bl, "2br":self.t2br, "2ibl":self.t2ibl, "2ibr":self.t2ibr, "2itl":self.t2itl, "2itr":self.t2itr, "2l":self.t2l, "2pd":self.t2pd, "2pl":self.t2pl, "2pr":self.t2pr, "2pu":self.t2pu, "2r":self.t2r, "2t":self.t2t, "2tl":self.t2tl, "2tr":self.t2tr, "3":self.t3, "3b":self.t3b, "3bl":self.t3bl, "3br":self.t3br, "3ibl":self.t3ibl, "3ibr":self.t3ibr, "3itl":self.t3itl, "3itr":self.t3itr, "3l":self.t3l, "3r":self.t3r, "3t":self.t3t, "3tl":self.t3tl, "3tr":self.t3tr, "4":self.t4, "4bl":self.t4bl, "4br":self.t4br, "4t":self.t4t, "4tl":self.t4tl, "4tr":self.t4tr, "5":self.t5, "5bl":self.t5bl, "5blr":self.t5blr, "5br":self.t5br, "5h":self.t5h, "5tbl":self.t5tbl, "5tbr":self.t5tbr, "5tl":self.t5tl, "5tlr":self.t5tlr, "5tr":self.t5tr, "5v":self.t5v, "5x":self.t5x, "6h":self.t6h, "6t":self.t6t, "6v":self.t6v, "7":self.t7, "7bl":self.t7bl, "7br":self.t7br, "7t":self.t7t, "7tl":self.t7tl, "7tr":self.t7tr, "8":self.t8, "8d":self.t8d, "8l":self.t8l, "8r":self.t8r}

        self.utexture_tags = {"1":self.u1, "1b":self.u1b, "1p":self.u1p, "1r":self.u1r, "1y":self.u1y, "2":self.u2, "2b":self.u2b, "2bl":self.u2bl, "2br":self.u2br, "2ibl":self.u2ibl, "2ibr":self.u2ibr, "2itl":self.u2itl, "2itr":self.u2itr, "2l":self.u2l, "2pd":self.u2pd, "2pl":self.u2pl, "2pr":self.u2pr, "2pu":self.u2pu, "2r":self.u2r, "2t":self.u2t, "2tl":self.u2tl, "2tr":self.u2tr, "3":self.u3, "3b":self.u3b, "3bl":self.u3bl, "3br":self.u3br, "3ibl":self.u3ibl, "3ibr":self.u3ibr, "3itl":self.u3itl, "3itr":self.u3itr, "3l":self.u3l, "3r":self.u3r, "3t":self.u3t, "3tl":self.u3tl, "3tr":self.u3tr, "4":self.u4, "4bl":self.u4bl, "4br":self.u4br, "4t":self.u4t, "4tl":self.u4tl, "4tr":self.u4tr, "5":self.u5, "5bl":self.u5bl, "5blr":self.u5blr, "5br":self.u5br, "5h":self.u5h, "5tbl":self.u5tbl, "5tbr":self.u5tbr, "5tl":self.u5tl, "5tlr":self.u5tlr, "5tr":self.u5tr, "5v":self.u5v, "5x":self.u5x, "6h":self.u6h, "6t":self.u6t, "6v":self.u6v, "7":self.u7, "7bl":self.u7bl, "7br":self.u7br, "7t":self.u7t, "7tl":self.u7tl, "7tr":self.u7tr, "8":self.u8, "8d":self.u8d, "8l":self.u8l, "8r":self.u8r}

        self.sky = pygame.transform.scale(pygame.image.load(os.path.join('finalProject/models/map', 'sky.png')), (room_settings.screen_width, room_settings.screen_height))
        self.Sky = pygame.Surface(self.sky.get_size(), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.SRCALPHA)
        self.Sky.blit(self.sky, (0,0))
        del self.sky
        self.size = room_settings.screen_tile
    def loadtexture(self, file, room_settings):
        bitmap = file
        surface = pygame.Surface((room_settings.screen_tile, room_settings.screen_tile), pygame.HWSURFACE|pygame.SRCALPHA|pygame.DOUBLEBUF)
        surface.blit(bitmap, (0,0))
        return surface
    def blocked_at(self, pos):
        if list(pos) in self.blocked:
            return True
        else:
            return False
    def speed_at(self, pos):
        if list(pos) in self.speed:
            return True
        else:
            return False

class CameraSettings():
    def __init__(self):
        self.spd = 1
        self.camerax = 0
        self.cameray = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    def update(self, deltatime, room_settings, player_settings, tiles, p):
        if tiles.speed_at((math.floor(p.x-.5), math.floor(p.y-.5))):
            self.spd = 1.5
        else:
            self.spd = 1
        if self.moving_left:
            if not tiles.blocked_at((math.floor(p.x-1), math.floor(p.y-.5))):
                self.camerax += deltatime * player_settings.p_speed_factor * self.spd
        elif self.moving_right:
            if not tiles.blocked_at((math.floor(p.x), math.floor(p.y-.5))):
                self.camerax -= deltatime * player_settings.p_speed_factor * self.spd
        elif self.moving_down:
            if not tiles.blocked_at((math.floor(p.x-.5), math.floor(p.y))):
                self.cameray -= deltatime * player_settings.p_speed_factor * self.spd
        elif self.moving_up:
            if not tiles.blocked_at((math.floor(p.x-.5), math.floor(p.y-1))):
                self.cameray += deltatime * player_settings.p_speed_factor * self.spd
