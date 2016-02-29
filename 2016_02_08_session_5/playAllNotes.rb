# playAllNotes
# @dataknut
# A simple SonicPi for loop used to play a sequence of increasing midi notes
# Try running it...
# When can you start to hear the note?
# When can you no longer hear it?

for l in 0..127
  puts l
  play l
  sleep 0.5
end