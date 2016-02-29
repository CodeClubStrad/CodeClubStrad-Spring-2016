# playAllNotes
# @dataknut
# A simple SonicPi for loop used to play a sequence of increasing midi notes
# Try running it...
# When can you start to hear the note?
# When can you no longer hear it?

# MIDI go from 0 to 127 (128 notes)
for note in 0..127
  # print the value of note to the console for feedback (in case we can't hear it)
  puts note
  # play the note
  play note
  # wait 1/2 a second
  sleep 0.5
end