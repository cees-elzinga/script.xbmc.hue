import xbmc
import xbmcgui
import xbmcaddon
import time
import sys
import colorsys
import os
import datetime

__addon__      = xbmcaddon.Addon()
__cwd__        = __addon__.getAddonInfo('path')
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ) )

sys.path.append (__resource__)

from settings import *
from tools import *

SCRIPTNAME = "XBMC Hue"

def log(msg):
  global SCRIPTNAME
  xbmc.log("%s: %s" % (SCRIPTNAME, msg))

log("Service started")
class MyPlayer(xbmc.Player):
  playingvideo = None

  def __init__(self):
    xbmc.Player.__init__(self)
  
  def onPlayBackStarted(self):
    if self.isPlayingVideo():
      self.playingvideo = True
      state_changed("started")

  def onPlayBackPaused(self):
    if self.isPlayingVideo():
      self.playingvideo = False
      state_changed("paused")

  def onPlayBackResumed(self):
    if self.isPlayingVideo():
      self.playingvideo = True
      state_changed("resumed")

  def onPlayBackStopped(self):
    if self.playingvideo:
      self.playingvideo = False
      state_changed("stopped")

  def onPlayBackEnded(self):
    if self.playingvideo:
      self.playingvideo = False
      state_changed("stopped")

class Hue:
  params = None
  connected = None
  last_state = None
  light = None

  def __init__(self, settings):
    self._parse_argv()
    self.settings = settings
    if self.settings.bridge_user not in ["-", "", None]:
      self.update_settings()

    if self.params == {}:
      if self.settings.bridge_ip not in ["-", "", None]:
        self.test_connection()
    elif self.params['action'] == "discover":
      log("Starting discover")
      notify("Bridge discovery", "starting")
      hue_ip = start_autodisover()
      if hue_ip != None:
        notify("Bridge discovery", "Found bridge at: %s" % hue_ip)
        username = register_user(hue_ip)
        log("Updating settings")
        self.settings.update(bridge_ip = hue_ip)
        self.settings.update(bridge_user = username)
        notify("Bridge discovery", "Finished")
        self.test_connection()
      else:
        notify("Bridge discovery", "Failed. Could not find bridge.")
    else:
      # not yet implemented
      log("unimplemented action call: %s" % self.params['action'])

    if self.connected:
      if self.settings.misc_initialflash:
        self.flash_lights()

  def flash_lights(self):
    self.light.flash_light()
    
  def _parse_argv( self ):
    try:
        self.params = dict(arg.split("=") for arg in sys.argv[1].split("&"))
    except:
        self.params = {}

  def test_connection(self):
    response = urllib2.urlopen('http://%s/api/%s/config' % \
      (self.settings.bridge_ip, self.settings.bridge_user))
    response = response.read()
    test_connection = response.find("name")
    if not test_connection:
      notify("Failed", "Could not connect to bridge")
      self.connected = False
    else:
      notify("XBMC Hue", "Connected")
      self.connected = True

  def dim_lights(self):
    self.light.dim_light(self.settings.dim_brightness)
        
  def brighter_lights(self):
    self.light.brighter_light()

  def update_settings(self):
    if self.settings.light == 0 and \
        (self.light is None or self.light.group is not True):
      self.light = Group(self.settings.bridge_ip, self.settings.bridge_user)

    elif self.settings.light > 0 and \
        (self.light is None or self.light.light != self.settings.light):
      self.light = Light(self.settings.bridge_ip, self.settings.bridge_user, self.settings.light)

def run():
  last = datetime.datetime.now()
  player = MyPlayer()
  while not xbmc.abortRequested:
    if datetime.datetime.now() - last > datetime.timedelta(seconds=1):
      # check for updates every 1s (fixme: use callback function)
      last = datetime.datetime.now()
      hue.settings.readxml()
      hue.update_settings()
    
    xbmc.sleep(500)

def state_changed(state):
  if state == "started":
    hue.light.get_current_setting()
  if state == "started" or state == "resumed":
    hue.dim_lights()
  elif state == "stopped" or state == "paused":
    hue.brighter_lights()

if ( __name__ == "__main__" ):
  settings = settings()
  hue = Hue(settings)
  while not hue.connected:
    time.sleep(1)
  run()
