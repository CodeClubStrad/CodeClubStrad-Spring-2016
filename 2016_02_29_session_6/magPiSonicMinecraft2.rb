# From MagPi article by Sam Aaron

live_loop :sand_storm do
  x, y, z = mc_location
  xd = rrand(-10, 10)
  zd = rrand(-10, 10)
  co = rrand(70, 130)
  synth :cnoise, attack: 0, release: 0.125, cutoff: co
  mc_set_block :sand, x + xd, y+20, z+zd

  bs = (ring :gold, :diamond, :glass)
  10.times do |xd|
  	10.times do |yd|
    	mc_set_block bs.choose, x + xd, y + yd, z
  	end
  end 
  sleep 0.125
end 

