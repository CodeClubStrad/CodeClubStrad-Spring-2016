# Session 4
In which we:
 * Part I - SonicPi
  * Attempted to run the pre-installed SonicPi but discovered it is v2.4 and won't run.
  * Persuaded @developius to spend the rest of the evening updating all the SD cards with the latest distros of everything!
 
 * Part II: Reverted to pythoning Minecraft Pi
  * Tracking our player using `mc.player.getPos()` - works 
  * Moving our player usng `mc.player.setPos(x,y,z)` - works 
  * Creating blocks using `mc.setBlock(x, y, z, <type>)` - works 
  * Creating regular shapes out of blocks using `mc.setBlocks(x, y, z, x2, y2, z2, <type>)
.` - works fine
  * Attempting to move intruders in 'our' world using `mc.entity.setPos(entityId,X,Y,Z)` - does not not work 
  * Attempting to set traps for intruders in 'our' world by combining `mc.entity.getPos(entityId)` with block creation/removal - does not not work 
