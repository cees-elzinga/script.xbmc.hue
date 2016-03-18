script.xbmc.hue
===============

![ScreenShot](http://meethue.files.wordpress.com/2013/01/plugin2.png?w=400)

An XBMC add-on that controls Philips Hue lights. It will automatically dim the lights as soon as a movie starts playing, and turns the lights back on once the movie is done.

Installation
------------

Download the add-on as a ZIP file. Open XBMC and go to:

`System -> Settings -> Add-ons -> Install from zip file`

Restart XBMC and configure the add-on:

`System -> Settings -> Add-ons -> Enabled add-ons -> Services -> XBMC Philips Hue -> Start bridge discovery`

Using "Start auto discovery of bridge IP and User" the "Bridge IP" and "Bridge User" are entered automatically.

Note for Raspberry Pi users: save the add-on configuration by exiting XBMC before shutting down the Pi completely.

Ambilight mode
--------------

If you'd like to use your lights in an ambilight mode you'll need the "ambilight" version of this add-on, available at: https://github.com/cees-elzinga/script.xbmc.hue.ambilight. In order for the ambilight mode to work you'll need to install the XBMC requests add-on first.

Release history
---------------
  * 2013-04-25 v0.2.3 Custom dimmed brightness
  * 2013-04-22 v0.2.2 Ignore the light if it's turned off. Only act on video playback (not music)
  * 2013-04-01 v0.2.1 Rename to scripts.xbmc.hue
  * 2013-02-25 v0.2.0 Improved handling for grouped lights
  * 2013-01-27 v0.1.0 Initial release 

Contributing
------------

Want to contribute? Great! I don't plan on actvily extending this code, but will accept push requests and help with bug reports. You can contact me on my Github profile page.

Feel free to fork away and have fun!

