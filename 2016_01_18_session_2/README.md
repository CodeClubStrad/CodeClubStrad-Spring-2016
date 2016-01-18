# Session 2
In which we:
 * tried to set up a proxy for a Raspberry Pi so it could connect to the internet from the school network:
  * see instructions on the [Pinet site](http://pinet.org.uk/articles/advanced/web-filtering.html#raspbian):
   1. Open a terminal on the Ubuntu server and enter `sudo ltsp-chroot --arch armhf` to enter the Raspbian chroot. We're not sure if we actually needed to do this on Debian?
   2. Enter `leafpad /etc/apt/apt.conf.d/10proxy` to create a text file of the right name in the right folder (directory) and open it with the leafpad text editor. We started off using nano but this was way too complex (yikes, keystroke commands!).
   3. Add in `Acquire::http::Proxy "http://proxy.gfl.suffolk.org.uk:8083"` and save it
   4. Possibly reboot the Pi using `sudo reboot` (this hung so we just pulled out the power)
   5. Test using the web browser - can you see https://github.com/CodeClubStrad/sessions/tree/master/2016_01_18_session_2?
  * Update: this didn't work. We're not sure if this was because the proxy was down or the instructions didn't work!

And then we:
 * made a (hollow) [room](https://arghbox.files.wordpress.com/2014/04/warehouse_a5.pdf)
 * learnt to comment our code - and why it's VITAL!
 * tried to combine last week's code on locating the position of a player with this week's room-builder to catch a player inside a sealed room made of a block of your choice.
 
We also learnt that:
 * joining other people's worlds & trashing them is fun for us but not for them
 * running clever block generation/trashing code can really slow your Pi - and even make Minecraft crash
 * that memory is a scarce resource which needs to be carefully managed!
