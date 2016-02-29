# playAllNotesLiveLoop
# @dataknut
# An improvement on the 'for' loop:
# A simple SonicPi live_loop used to play a sequence of increasing midi notes
# In this case we have to stop (break) the loop at note 127
# This will throw a not very pretty exception
# Try running it...
# When can you start to hear the note?
# When can you no longer hear it?

# start with note 0
note = 0
live_loop :playAllNotes do
  # print the note value to the console for feedback (in case we can't hear it!)
  puts note
  # now play the note
  play note
  # add one to the value of note
  note = note + 1
  # check the value of note - MIDI only goes up to 127 (128 notes)
  if note > 127
  	puts "Midi note out of range (> 127)"
    # stop the loop (creates a not very pretty error)
    break
  end
  # wait for 1/2 a second
  sleep 0.5
end