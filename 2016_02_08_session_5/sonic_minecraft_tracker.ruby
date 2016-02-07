# Welcome to Sonic Pi v2.7
# Code by dataknut: trackers player's location in minecraft and plays a
# note defined by x (note) y (amplitude) and z (attack)
live_loop :mc_play do

  puts mc_location
  # mc_message "Location is " + mc_location
  # convert x value to a valid midi note in range 50 - 110 ish
  # max x/y/z value = 128 in minecraft
  x = 50+((mc_location[0].abs/128)*60)
  y = (mc_location[1].abs/150)*2
  z = mc_location[2].abs/150
  puts x
  play x, amp: y, attack: z
  sleep 1
end
