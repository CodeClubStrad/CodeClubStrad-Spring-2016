# Experiments with MinecraftPi entities & python

Context: Minecraft Pi & Python (IDLE 2) runnng on Debian (?) v? on Raspberry Pi Model B purchased December 2015

Ref: http://www.stuffaboutcode.com/p/minecraft-api-reference.html

In what follows we refer to the local player as the 'home' player and any players who join that world as 'away' players.

Aim: to develop traps for and defences against other Minecraft Pi players who might join (and attempt to trash) our world as a precursor to developing a multiplayer 'Hunger Games' inspired arena for Minecraft Pi.

## Setting player positions in Minecraft Pi multi-player games
According to the API reference there are two ways to do this:
 * `mc.player.setPos(x,y,z)` - which can only set the 'home' player's location or by 'away' players to set their own location;
and
 * `mc.player.setPos(entityId,x,y,z)` - using an entity ID obtained via `mc.getPlayerEntityIds()` - which should be able to set any player's location.

But the two functions have the same names. We thought the function might count it's arguments to know what to do but it doesn't - the second form simply uses the entityID as the x co-ord and moves the 'home' player. This can have startling results if the ID is a large integer!

So maybe there is a typo in the api-reference. Perhaps it should read:
 * `mc.entity.setPos(entityId,x,y,z)` - typo & possible bug confirmed by [@martinohanlon](https://twitter.com/martinohanlon/status/690307404655886336)

This seems to work - we can teleport both the 'home' player (as we would with `mc.player.setPos(x,y,z)`) and we can also move 'away' players. Or at least the 'away' players we see in our world _appear_ to move. BUT they do not move at their own client end. So we think we've moved the 'away' players and tracking their position using `mc.entity.getPos(entityID)` confirms that our Minecraft client (and thus our world view) thinks they've been moved. But as far as their user is concerned, nothing happens.

(A possibly relevant observation: if we move the 'away' players up into the sky using (e.g.) `mc.entity.setPos(entityId,20,20,20)`, they do not then fall to the ground, even if they're not in fly mode anymore... And the away player's user does not experience any move at all!)

## Creating/changing blocks in multi-player Minecraft Pi games
If we can't actually move 'away' players then perhaps we can just trap them by making holes under them or encasing them in blocks?

Unfortunately this appears not to work either. Any blocks created (or converted to air) by the API after 'away' players have joined the world seem to remain invisible to (and have no effect on) 'away' players. However blocks created before the 'away' player joins the world are visible to them.

Update - we are not sure if this is true in all situations and are trying to systematically replicate and document what does and does not work!