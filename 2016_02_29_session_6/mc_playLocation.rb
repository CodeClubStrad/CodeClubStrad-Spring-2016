# mc_playLocation
# A simple SonicPi live loop to play a note that represents
# our Minecraft Pi location (x,y,z) values
# uses pan (left vs right speaker) for x - see 2.2 Synth Options
# uses the note for y (height)
# uses amp (amplitude) for z - see 2.2 Synth Options

# @dataknut
live_loop :mc_playLocation do
  # post a message to Minecraft to prove the connection is working
  mc_message "Hello from Sonic Pi"
  
  # Turn x into a useful pan value
  # Pan has the ranhe -1 (left) to 1 (right)
  # Use the fact that the MinecraftPi world goes from -128 to 128 on any dimension
  # this should create a value between -1 and +1
  xPan = mc_location[0]/128

  # Turn y into a useful height note (see mc_playHeight.rb)
  yNote = 90 + (mc_location[1]/128)*30

  # Turn z in to a useful amp value - between 0 (no sound) -> 1 (normal) and 2 (loud)
  zAmp = (mc_location[2].abs/128)*2

  puts xPan yNote zAmp
  play yNote, pan: xPan, amp: zAmp, release: 0.5
  sleep 0.5
end