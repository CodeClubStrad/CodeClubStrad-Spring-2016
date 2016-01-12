# This is a comment - they are very useful for making sense of your code
 
# import the minecraft module to Python
import mcpi.minecraft as minecraft
# import the time module - we will be using a function from it later
import time

# Set up the connection to the running minecraft
mc = minecraft.Minecraft.create()

# Start a never-ending loop to locate the player (you!)
# Note the indentation - this is crucial to Python!
while True:
	pos = mc.player.getPos()
	x = pos.x
	y = pos.y
	z = pos.z

	# we're going to use a flower block (38) - you could try a different kind
	# see http://www.stuffaboutcode.com/p/minecraft-api-reference.html for a list
	blockType = 38

	# now put a block of this type at the user's current location
	mc.setBlock(x, y, z, blockType)

	# pause for 0.5 seconds before we try to drop another block
	# this will make the blocks appear 0.5 seconds 'apart'
	time.sleep(0.5)