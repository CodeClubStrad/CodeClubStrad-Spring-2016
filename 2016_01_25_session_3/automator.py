# Python code to track players and print location to console whilst moving ourselves
# Code: @dataknut @developius
# with inspiration from:
# - https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/
# - http://www.stuffaboutcode.com/p/adventures-in-minecraft.html

# import the libraries we need
import mcpi.minecraft as minecraft
import time # needed for the sleep
import random

# Set up the connection to the running minecraft
mc = minecraft.Minecraft.create()
    
# Start a never-ending loop to move me and locate all players (including me)
# Note the indentation - this is crucial to Python!
while True:
	# move ourselves from wherever we are
	mypos = mc.player.getPos()
	distance = random.randint(-5,+5) # move randomly +/- 
	# Warning - this may well take you under ground!

	mc.player.setPos(mypos.x + distance, mypos.y + distance, mypos.z + distance)
	
	# now get the list of players (could be just 1)
	playerIDs = mc.getPlayerEntityIds()

	for player in playerIDs:
		pos = mc.entity.getPos(player) # check where they are
		print("Player %s now at: %s" % (player,pos)) # print out
		# no sleep here - run round this list as quickly as possible

	print("Wait 1 sec")
	time.sleep(1) # wait for 1 second before checking again