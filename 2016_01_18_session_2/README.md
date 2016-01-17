# Session 2
In which we:
 * learn how to set up a proxy for a Raspberry Pi so it can connect to the internet from the school network:
  * see instructions on the [Pinet site](http://pinet.org.uk/articles/advanced/web-filtering.html#raspbian)
  1. Open a terminal on the Ubuntu server and enter `sudo ltsp-chroot --arch armhf` to enter the Raspbian chroot.
  2. Enter `nano /etc/apt/apt.conf.d/10proxy` to create a text file there and open it with the nano text editor.
  3. Add in `Acquire::http::Proxy "http://proxy.gfl.suffolk.org.uk:8083"` and save it
  4. Possibly reboot the Pi using `sudo reboot'
  5. Test using the web browser - can you see https://github.com/CodeClubStrad/sessions/tree/master/2016_01_18_session_2?

And then we:
 * make a (hollow) [room](https://arghbox.files.wordpress.com/2014/04/warehouse_a5.pdf)
 * use the console to [send chat](https://arghbox.files.wordpress.com/2014/04/chat_a5.pdf) and learn how to end a while loop with a specified command
 * use an if statement to test of the player is on water and if so, [freeze it](https://arghbox.files.wordpress.com/2014/04/freeze_a5.pdf)!
 * learn to comment our code - and why it's VITAL!
 * combine these to catch your player inside a block of ice and give a text feedback when they're caught.
 
Once we've done all that we will all join the same world and:
 * use the console to practice getting a list of users
 * catch a random (or specific) player in a bloc of ice
 * write a programme to catch all of the players in blocks of ice before they can smash their way out!