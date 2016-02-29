# mc_playLocation
# Author: @dataknut
# License: https://github.com/CodeClubStrad/CodeClubStrad-Spring-2016/blob/master/LICENSE.md

# A simple SonicPi live loop to play a note that represents
# our Minecraft Pi location (x,y,z) values
# uses pan (left vs right speaker) for x - see 2.2 Synth Options
# uses the note for y (height)
# uses amp (amplitude) for z - see 2.2 Synth Options

# Set this loop running and then move around in MinecraftPi

# post a message to Minecraft to prove the connection is working
mc_message "Hello from Sonic Pi"

live_loop :mc_playLocation do
  # put our location x,y,z values into a variable - saves connecting to minecraft lots of times
  myLoc = mc_location

  # Turn x into a useful pan value
  # Pan has the range -1 (left) to 1 (right)
  # Use the fact that the MinecraftPi world goes from -128 to 128 on any dimension
  # this should create a value between -1 and +1
  xPan = myLoc[0]/128

  # Turn y into a useful height note (see mc_playHeight.rb)
  yNote = 90 + (myLoc[1]/128)*30

  # Turn z in to a useful amp value - between 0 (no sound) -> 1 (normal) and 2 (loud)
  # See how we have to use .abs to always give a positive value
  zAmp = (myLoc[2].abs/128)*2

  # print location
  puts myLoc

  # the converted values get printed by play to the console anyway
 
  # Now play the note
  play yNote, pan: xPan, amp: zAmp, release: 0.5
  # Wait 1/2 a second
  sleep 0.5
end