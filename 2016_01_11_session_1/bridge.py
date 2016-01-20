# This is a comment - they are very useful for making sense of your code
# Make a magic bridge
# Inspired by:
# Craig Richardson's fantastic https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/

from time import sleep
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

air = 0
grass = 2
flower = 38
water = 8
water_stationary = 9

while True:
	x, y, z = mc.player.getPos()  # player position (x, y, z)
	block_beneath = mc.getBlock(x, y-1, z)  # block ID

	if block_beneath == water or block_beneath == water_stationary or block_beneath == air:
		mc.setBlock(x, y-1, z, grass)
		print("saving your life")
	sleep(0.01)
