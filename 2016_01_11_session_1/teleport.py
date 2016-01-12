# This is a comment - they are very useful for making sense of your code
 
# import the minecraft library to Python
import mcpi.minecraft as minecraft

# Set up the connection to the running minecraft
mc = minecraft.Minecraft.create()

# Let's set a location co-ordinate
x = 10
y = 11
z = 12

# now move the player (you!) to the location
mc.player.setPos(x, y, z)