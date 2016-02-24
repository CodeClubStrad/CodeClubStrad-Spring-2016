# mc_PlayHeight
# A simple SonicPi live loop to play a note that represents
# our Minecraft Pi height (y) value
# @dataknut
live_loop :mc_playHeight do
  #mc_message "Hello from Sonic Pi"
  puts mc_location[1]
  # We could play the note that matches the y location:
  # play mc_location[1]
  # Why does this often not work?  
  # Correct - midi notes lie in the range 0 - 127 but -128 < y < 128
  # Also you probably can't hear anything outside the range 50 - 110 (depending how old you are :-)
  # So we need to transform the y value into something more helpful

  # Let's assume 90 is the middle of the range we can hear
  # MinecraftPi is -128 < y < 128 (a small world :-)
  # So take the value of y and work out it's proportion of 128 (max depth/height)
  # Find the note that is that proportion of half our range (30)
  # Add/substract that to/from 90
  heightNote = 90 + (mc_location[1]/128)*30
  puts heightNote
  play heightNote, release: 0.5
  sleep 0.5
end