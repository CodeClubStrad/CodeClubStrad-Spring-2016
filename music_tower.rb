use_synth :piano
x,y,z = mc_location
blocks = (ring :gold, :diamond, :sand, :water, :lava)
live_loop :sand_storm do
  rand_x = rrand(x+1,x+11)
  rand_z = rrand(z+1,z+11)
  note = rand_i(60..110)
  new_y = (note - y)/4
  mc_set_block blocks.choose, rand_x, new_y, rand_z
  play note, release: 0.3
  sleep 0.5
end

live_loop :beats do
  sample :bd_haus, amp:2, cutoff: 100
  sleep 0.5
end