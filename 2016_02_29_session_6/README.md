# Session 6: Linking SonicPi and MinecraftPi
In which we attempt to connect Sonic Pi to MinecraftPi. SonicPi will automatically connect to MinecraftPi if it is running…

## Basic SonicPi <-> MinecraftPi functions
Look at Section 11 of the SonicPi Tutorials:
* `mc_message “text”`
 * -> sends a message to the MinecraftPi chat
* `mc_location`
 * -> returns a list of the current player location (x,y,z)
* `mc_teleport x, y, z`
 * -> moves the player to the location given by x,y,z
* `mc_set_block :type, x, y, z`
 * -> creates a block of type ‘type’ at x,y,z
* `mc_get_block x, y, z`
 * -> returns the kind of block at that location

## Things to try
 * [mc_playHeight](mc_playHeight.rb) - A simple SonicPi live_loop to play a note that represents our Minecraft Pi height (y) value - a higher note will represent being higher up in the world
 * [mc_playLocation](mc_playLocation.rb) - A simple SonicPi live loop to play a note that represents our Minecraft Pi location (x,y,z) values:
  * uses pan (left vs right speaker) for x - see 2.2 Synth Options
  * uses the note for y (height)
  * uses amp (amplitude) for z - see 2.2 Synth Options

## More fun
Look at the MinecraftPi/Sonic-Pi examples in Appendix A6 and A8 in the SonicPi v2.9 Tutorials. If you have version 2.7 and don't want to upgrade (why?) you can find them on [github](https://github.com/samaaron/sonic-pi/tree/master/etc/doc/tutorial/en). 

## Another big list of block types - useful for `mc_set_block`
:air :stone :grass :dirt :cobblestone :wood_plank :sapling :bedrock :water_flowing :water :water_stationary :lava_flowing :lava :lava_stationary :sand :gravel :gold_ore :iron_ore :coal_ore :wood :leaves :glass :lapis :lapis_lazuli_block :sandstone :bed :cobweb :grass_tall :flower_yellow :flower_cyan :mushroom_brown :mushroom_red :gold_block :gold :iron_block :iron :stone_slab_double :stone_slab :brick :brick_block :tnt :bookshelf :moss_stone :obsidian :torch :fire :stairs_wood :chest :diamond_ore :diamond_block :diamond :crafting_table :farmland :furnace_inactive :furnace_active :door_wood :ladder :stairs_cobblestone :door_iron :redstone_ore :snow :ice :snow_block :cactus :clay :sugar_cane :fence :glowstone_block :bedrock_invisible :stone_brick :glass_pane :melon :fence_gate :glowing_obsidian :nether_reactor_core
