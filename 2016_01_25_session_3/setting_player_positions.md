# Setting player positions in multi-player games
According to http://www.stuffaboutcode.com/p/minecraft-api-reference.html there are two ways to do this:
 * `mc.player.setPos(0.0,0.0,0.0)` - which can only set our own player's location
and
 * `mc.player.setPos(entityId,0.0,0.0,0.0)` - using an entity ID obtained via `mc.getPlayerEntityIds()` - which should be able to set any player's location.

But the two functions have the same names. We thought the function might count it's arguments to know what to do but it doesn't - the second form simply uses the entityID as the x co-ord and moves our player. With startling results if the ID is a large integer.

So maybe there is a typo in the api-reference. Perhaps it should read:
 * `mc.entity.setPos(entityId,0.0,0.0,0.0)`

This seems to work - we can manipulate both ourselves (as we would with `mc.player.setPos(0.0,0.0,0.0)`) and we can also move another player. Or at least the 'other' players we see in our world appear to move. BUT they do not move at their own client end. So we think we've moved them and tracking their position using mc.entity.getPos(entityID) confirms that our Minecraft client (and thus our world view) thinks they've been moved. But as far as their user is concerned, nothing happens!

(A possibly relevant observation: if we move the other player up into the sky using (e.g.) `mc.entity.setPos(entityId,20,20,20)`, they do not then fall to the ground...!)

What are we missing?