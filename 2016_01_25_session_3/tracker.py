# Python code to track players and print location to console
# Code: @dataknut @developius
# with inspiration from:
# - https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/
# - http://www.stuffaboutcode.com/p/adventures-in-minecraft.html

# import the libraries we need
import mcpi.minecraft as minecraft
import time # needed for the sleep

# Set up the connection to the running minecraft
mc = minecraft.Minecraft.create()
    
# Start a never-ending loop to locate players
# Note the indentation - this is crucial to Python!
while True:
	# get the list of players (could be just 1)
    playerIDs = mc.getPlayerEntityIds()
    for player in playerIDs: 
        pos = mc.entity.getPos(player) # check where they are
        print("Player %s now at: %s" % (player,pos))
        # no sleep here - run round this list as quickly as possible
    
    time.sleep(1) # wait for 1 second before checking again
   
