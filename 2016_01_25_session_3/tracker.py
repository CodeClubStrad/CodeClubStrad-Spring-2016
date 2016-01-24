# tracker.py
# https://github.com/CodeClubStrad/CodeClubStrad-Spring-2016/blob/master/2016_01_25_session_3/tracker.py
# Python code to track the number players and print location to the shell
# Code: @dataknut @developius
# with inspiration from:
# - https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/
# - http://www.stuffaboutcode.com/p/adventures-in-minecraft.html

# import the libraries we need
import mcpi.minecraft as minecraft
import time # needed for the time.sleep at the end

# Set up the connection to the running minecraft
mc = minecraft.Minecraft.create()
    
# Start a never-ending loop to locate players
# Note the indentation - this is crucial to Python!
while True:
	# get the list of players (could be just 1)
    playerIDs = mc.getPlayerEntityIds() # playerIDs will be a list of 1 or more IDs
    
    if len(playerIDs) > 1: 
    	# check the length of the variable playerIDs - if there's more than 1 ID in the
    	# list then we must have an intruder
        #print("Intruders!") # print to the shell if you wish 
        mc.postToChat("Intruders!") # give warning to Minecraft chat (tends to mask the screen)

    for player in playerIDs: # loop over each player ID 
        pos = mc.entity.getPos(player) # check where this player is
        print("Player %s now at: %s" % (player,pos)) # print out where they are to the shell
        # This is where you could set ambushes - but make sure you don;t ambush yourself!
        # Hint: the first player in the list is (we think) the 'home' player
        
    print("Wait 1 second")
    time.sleep(1) # wait for 1 second before checking the number of players again
   
