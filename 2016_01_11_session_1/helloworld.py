# This is a comment - they are very useful for making sense of your code
# Tell the user where the player is via the chat text
# Inspired by:
# Craig Richardson's fantastic https://arghbox.wordpress.com/2014/04/25/minecraft-pi-recipe-cards/

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat(mc.player.getPos())
