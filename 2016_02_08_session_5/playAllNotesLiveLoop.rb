# playAllNotesLiveLoop
# @dataknut
# A simple SonicPi live_loop used to play a sequence of increasing midi notes
# In this case we have to stop (break) the loop at note 127
# This will throw a not very pretty exception
# Try running it...
# When can you start to hear the note?
# When can you no longer hear it?

note = 0
live_loop :playAllNotes do
  note = note + 1
  if note > 127
    puts "Midi note out of range (> 127)"
    break
  end
  puts note
  play note
  sleep 0.5
end