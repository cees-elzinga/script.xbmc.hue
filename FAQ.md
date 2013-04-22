"Use all lights" doesn't work for me
------------------------------------

If the add-on is configured to "Use all lights", bulb number 2 has a special function. This bulb is "leading", ie the settings from this bulb are used for the whole group. Make sure this light is turned on when you start XBMC. If not, the add-on thinks the complete group is turned off.

This works perfect for me. I can also imagine it doesn't for you. If so, let me know and I might take some time and make this optional or something.

I would like to use only 2 lamps for ambilight
----------------------------------------------

Currently, the only supported modes are "all lights", or "1 single bulb".

A work-around is to create a new group for those two lights in the official Hue app (or any other tool). Remember the id of the group. Then you have to dive into the code (a little), specifically the file resources/lib/tools.py. Search for all occurrences of “http://%s/api/%s/groups/0/action” and change the “0″ to the id of your group, probably “1″.
