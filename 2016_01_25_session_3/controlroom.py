# controlroom.py
# https://github.com/CodeClubStrad/CodeClubStrad-Spring-2016/blob/master/2016_01_25_session_3/tracker.py
# Python code to attack players 
# Code: @developius
# with inspiration from:
# - https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/
# - http://www.stuffaboutcode.com/p/adventures-in-minecraft.html
# - The Hunger Games!

import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3 as Vec3
import time
import math
import random

class ControlRoom:
    def __init__(self, mc):
        """ pass me your minecraft.Minecraft.create() object please! """
        
        self.mc = mc
        self.autojump = False
        self.worldImmutable = False
        self.nametags = True

        self.mc.setting("autojump", self.autojump)
        self.mc.setting("world_immutable", self.worldImmutable)
        self.mc.setting("nametags_visible", self.nametags)

    def toggleAutoJump(self):
        """ toggle auto jump setting """
        
        self.autojump = not self.autojump
        self.mc.setting("autojump", self.autojump)
        return(self.autojump)
    
    def toggleWorldImmutable(self):
        """ toggle world immutable setting """
        
        self.worldImmutable = not self.worldImmutable
        self.mc.setting("world_immutable", self.worldImmutable)
        return(self.worldImmutable)

    def toggleNametags(self):
        """ toggle nametag visibility """
        
        self.nametags = not self.nametags
        self.mc.setting("nametags_visible", False)
        return(self.nametags)
        
    def tree(self, x, y, z, wood = block.LEAVES.id, leaves = block.LEAVES.id):
        """ make a tree at x, y, z with optionally specified wood and leaves """
        
        self.mc.setBlocks(x,y,z, x,y+6,z, wood)
        self.mc.setBlocks(x+2,y+4,z+2, x-2,y+5,z-2, leaves)
        
        self.mc.setBlocks(x+3,y+4,z-1, x,y+5,z+1, leaves)
        self.mc.setBlocks(x-1,y+4,z+3, x+1,y+5,z, leaves)
        self.mc.setBlocks(x-3,y+4,z-1, x-3,y+5,z+1, leaves)
        self.mc.setBlocks(x-1,y+4,z-3, x+1,y+5,z, leaves)

        self.mc.setBlocks(x+1,y+6,z+1, x+2,y+6,z-1, leaves)
        self.mc.setBlocks(x-1,y+6,z+1, x-2,y+6,z-1, leaves)
        self.mc.setBlocks(x+1,y+6,z-1, x-1,y+6,z-2, leaves)
        self.mc.setBlocks(x+1,y+6,z+1, x-1,y+6,z+2, leaves)

        self.mc.setBlock(x,y+7,z, leaves)
        self.mc.setBlock(x+1,y+7,z, leaves)
        self.mc.setBlock(x-1,y+7,z, leaves)
        self.mc.setBlock(x,y+7,z+1, leaves)
        self.mc.setBlock(x,y+7,z-1, leaves)

        self.mc.setBlock(x,y+8,z, leaves)

    def flowingWall(self, x, y, z, length = 2, height = 4, threat = "water"):
        """ make a flowing wall of either lava or water """
        
        if threat == "water": b = block.WATER_FLOWING.id
        if threat == "lava": b = block.LAVA_FLOWING.id
        self.mc.setBlocks(x - (length/2), y, z, x, y + height, z + (length/2), b)

    def groundLevel(self, x, z):
        """ find out where ground level is at x, z """
        
        y = -5 # 5 below sea level
        ground = False
        while not ground:
            y+=1
            b = self.mc.getBlock(x, y, z)
            if (b == block.AIR.id or b == block.SNOW.id): # if the block we've selected is air
                if (b == block.SNOW.id): self.mc.setBlock(x, y - 1, z, block.AIR.id)
                ground = True # we're at ground level
        return(y) # return the current y value

    def distance(self, x1, y1, z1, x2, y2, z2, height = False):
        """ calculate the distance between two points, optionally including height """
        
        xd = x1 - x2
        zd = z1 - z2
        if (height):
            yd = y1 - y2        
            d = math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
        else:
            d = math.sqrt((xd*xd) + (zd*zd))
        return(d)
    
    def randomCoordinates(self):
        """ generate some random coordinates at ground level """
        
        x = random.randint(-128, 128)
        z = random.randint(-128, 128)
        y = self.groundLevel(x, z)
        return {"x": x,
                "y": y,
                "z": z
                }
    
    def chase(self, wood = block.WOOD.id, leaves = block.LEAVES.id, randomplayer = False, player = None, threat="tree"):
        """ chase a player with the specified threat """
        
        start = time.time()
        if randomplayer:
            player = random.choice(self.mc.getPlayerEntityIds())
        if not player:
            player = self.mc.getPlayerEntityIds()[0]
        pos = self.mc.entity.getPos(player)
        origin = self.randomCoordinates()
        if threat == "trees":
            self.tree(origin['x'], origin['y'], origin['z'], wood, leaves)
            increment = 5
        else:
            self.flowingWall(origin['x'], origin['y'], origin['z'], length = 5, threat=threat)
            increment = 1

        distance = self.distance(pos.x, pos.y, pos.z, origin['x'], origin['y'], origin['z'])
        currentX = origin['x']
        currentZ = origin['z']
        while distance > 5:
            if (currentX < pos.x): currentX += increment
            if (currentX > pos.x): currentX -= increment
            if (currentZ < pos.z): currentZ += increment
            if (currentZ > pos.z): currentZ -= increment
            pos = self.mc.entity.getPos(player)
            currentY = self.groundLevel(currentX, currentZ)
            distance = self.distance(pos.x, pos.y, pos.z, currentX, currentY, currentZ)
            print(distance)
            b = self.mc.getBlock(currentX, currentY-1, currentZ)
            if (b != leaves):
                if threat == "trees":
                    self.tree(currentX, currentY, currentZ, wood, leaves)
                else:
                    self.flowingWall(currentX, currentY, currentZ, length = 5, threat=threat)
            time.sleep(0.5)
        duration = time.time() - start
        return(duration)
            
    def console(self):
        """ opens a console for interfacing with the ControlRoom """
        
        command = raw_input("> ")
        while command != "Q":
            if (command == "chase"):
               self.chase(block.OBSIDIAN.id, block.GLOWING_OBSIDIAN.ID)
            if (command == "ls"):
                for entityId in self.mc.getPlayerEntityIds():
                    print entityId
            if (command == "autojump"):
                 print("Auto jump is now " + ("enabled" if self.toggleAutoJump() else "disabled"))
            if (command == "immutable"):
                print("World is now " + ("immutable" if self.toggleWorldImmutable() else "mutable"))
            if (command == "nametags"):
                print("Nametags are now " + ("visible" if self.toggleNametags() else "invisble"))
            command = raw_input("> ")

    def circlePath(self, ox, oy, oz, r):
        """ returns a circle path for the circle specified """

        circlePath = {"coords": []}
        for i in range(0,361):
            ri = math.radians(i)
            x = ox + r * math.cos(ri)
            z = oz + r * math.sin(ri)
            circlePath['coords'].append(Vec3(x,oy,z))
        return(circlePath)