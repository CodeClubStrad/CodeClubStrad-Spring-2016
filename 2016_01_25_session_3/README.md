# Session 3
In which you will:
 * Part I - Find your player
  * Connect everything together except the ethernet cable (power plug last!) and start the Raspberry Pi. Type startx and return if you need to.
  * Open Minecraft Pi
  * Open IDLE (v2) and arrange the "Python Shell" window so you can see it and the Minecraft window (so you can easily switch between the two)
  * In the shell window load the minecraft library by entering: `import mcpi.minecraft as minecraft` and press return.
  * Now connect to the minecraft gamne by entering: `mc = minecraft.Minecraft.create()` and pressing return.
  * Now you need to work out how many players are in your game. To do this type `mc.getPlayerEntityIds()` in the shell and press return. How many numbers are there? These numbers (IDs) represent the players and there should be only one!
  * To find out where the (your) player is type `mc.entity.getPos(ID)` where ID is the number you got above.
  * To smarten this up a bit you can make a nice print statement by typing `print("Player at: %s" % (mc.entity.getPos(ID)))`
 
 * Part II: Develop an intruder alarm to detect players entering your world
  * Now plug in your ethernet and invite someone to join your world
  * Use a `while True:` loop to continuously check how many players there are and then to print their location to the shell. 
  * You will need to use a `for` loop because `mc.getPlayerEntityIds()` will give you a list of 1 or more players. 
  * Give the user a message in the minecraft chat if there is an intruder (i.e. more than 1 player in the world). You will need to use an `if` statement to do that.
  * The complete code should look something like the code in [tracker.py](tracker.py)
 
 * Part III: Over to you
  * Now develop this further to make your own intruder traps/ambushes etc

Remembering that:
 * we need to comment our code!
 * joining other people's worlds & trashing them is fun for us but not for them
 * running clever block generation/trashing code can really slow your (or someone else's) Pi - and even make Minecraft crash
 * memory is a scarce resource which needs to be carefully managed
 * if all else fails and you can't see off the intruders - pull out the ethernet cable!
