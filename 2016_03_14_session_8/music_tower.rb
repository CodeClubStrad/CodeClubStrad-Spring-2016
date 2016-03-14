# Demonstrating creating blocks based on musical parameters
# @dataknut

# extensions:
# use pan to make sound go left/right depending on random value of x diff?
# set block type based on note - e.g. if divides by some number without a remainder?
# experiment with different block types to have different effects
# use some real music instead of random notes!!

# just to give a background beat...
live_loop :beats do
  sample :bd_haus, amp:2, cutoff: 100
  sleep 0.5
end

use_synth :piano
x,y,z = mc_location

# list of block types to choose from
# by using sand we get some interesting effects
blocks = (ring :gold, :diamond, :sand, :glass
          )

live_loop :block_wall do
  # calculate new x value 10-40 blocks away
  new_x = rrand(x+10,x+40)
  # make a tower (by varying z) rather than just a wall
  new_z = rrand(z+10,z+40)
  # random note (integer)
  note = rand_i(60..110)
  # reduce the note value so the block position is visible
  new_y = y + ((note)/4)
  # create random block from list at calculated location
  mc_set_block blocks.choose, new_x, new_y, new_z
  # play the note
  play note
  sleep 0.2
end