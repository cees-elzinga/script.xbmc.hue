script.xbmc.hue
===============

![ScreenShot](http://meethue.files.wordpress.com/2013/01/plugin2.png?w=400)

This is an XBMC add-on that controls Philips Hue lights. It will automatically dim the lights as soon as a movie starts playing, and turns the lights back on once the movie is done The add-on is made to be portable and works out of the box. Follow the installation instructions and you're ready to go.

Installation
------------

Download the add-on as a ZIP file. Open XBMC and go to:

System -> Settings -> Add-ons -> Install from zip file

Restart XBMC and configure the add-on:

System -> Settings -> Add-ons -> Enabled add-ons -> Services -> XBMC Philips Hue

Note for Raspberry Pi users: To save the add-on configuration exit XBMC first before shutting down the Pi.

Ambilight mode
--------------

If you'd like to use your lights in an ambilight mode you'll need the "ambilight" version of this add-on, available at: https://github.com/cees-elzinga/script.xbmc.hue.ambilight. In order for the ambilight mode to work you'll need to install the Python PIL library first.

Donations
---------
If you like the add-on, donations are always welcome :)

[![PayPal]( https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=48ZKAZK6QHNGJ&lc=NL&item_name=script%2exbmc%2ehue&currency_code=EUR)

Release history
---------------
  * 2013-04-01 v0.2.1 Rename to scripts.xbmc.hue
  * 2013-02-25 v0.2.0 Improved handling for grouped lights
  * 2013-01-27 v0.1.0 Initial release 

Contributing
------------

Want to contribute? Great! I don't plan on actvily extending this code, but will accept push requests and help with bug reports. You can contact me on my Github profile page.

Feel free to fork away and have fun!

