# Python code to check if you have intruders in your world and if so, to do something to them
# to stop them messing up your world
# Note that this will only catch the intruding players - it won't prevent code attacks!
# Code: @dataknut @developius
# with inspiration from:
# - https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/
# - http://www.stuffaboutcode.com/p/adventures-in-minecraft.html

# import the libraries we need
import mcpi.minecraft as minecraft
import time # needed for the sleep

# Set up the connection to the running minecraft
mc = minecraft.Minecraft.create()

crown = 78 # set block type - see http://www.stuffaboutcode.com/p/minecraft-api-reference.html for a list


# make a crown over me so I can identify myself
# this funciton always returns the position of me (whichever world I'm in)
mypos = mc.player.getPos()
mc.setBlock(mypos.x, mypos.y + 2, mypos.z, crown) # put my crown over my head
# you can also set the block type by using e.g. mc.setBlock(mypos.x, mypos.y + 2, mypos.z,block.DIRT.id)

# save my old position so I can delete the crown when I've moved otherwise I'll leave a trail of crowns behind me!
myoldpos = mypos
    
# Start a never-ending loop to locate any intruders
# Note the indentation - this is crucial to Python!
while True:
	# First mcheck if I have moved
    mypos = mc.player.getPos() # find me
    # only create the crown if I have moved (saves rendering time)
    if mypos != myoldpos:
        mc.setBlock(myoldpos.x, myoldpos.y + 2, myoldpos.z, 0)
        mc.setBlock(mypos.x , mypos.y + 2, mypos.z, crown)
        myoldpos = mypos # save mypos again for next time
    
    # get the list of players (could be just 1)
    playerIDs = mc.getPlayerEntityIds()
	#print(playerIDs)
    if len(playerIDs) > 1:
        #print("Intruders!")
        mc.postToChat("Intruders!") # give warning

        for player in playerIDs[1:]: # the first entity is me (we think!) so start from the second which will be index 1
            mc.player.setPos(player,25,25,25) # throw them high in the sky
            mc.postToChat("Intruder ID %s captured!" % (player)) # give feedback
            #print("Intruder ID %s : %s" % (player,entityPos))

        time.sleep(1) # this gives the captured player time to descend slowly under gravity before being caught again
   
