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
  def __init__(self):
    xbmc.Player.__init__(self)

  def onPlayBackStarted(self):
    state_changed("started")

  def onPlayBackPaused(self):
    state_changed("paused")

  def onPlayBackResumed(self):
    state_changed("resumed")

  def onPlayBackStopped(self):
    state_changed("stopped")

class Hue:
  params = None
  connected = None
  last_state = None
  lights = None

  def __init__(self, settings):
    self._parse_argv()
    self.settings = settings

    if self.params == {}:
      if self.settings.bridge_ip != "-":
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
    for light in self.used_lights():
        light.flash_light()
    
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
    for light in self.used_lights():
        light.dim_light()
        
  def brighter_lights(self):
    for light in self.used_lights():
        light.brighter_light()

  def active_light(self, light):
    if self.lights == None:
      return False
    else:
      return len([l for l in self.lights if l.light == light]) == 1

  def used_lights(self):
    if self.settings.light_1 != self.active_light(1) or \
       self.settings.light_2 != self.active_light(2) or \
       self.settings.light_3 != self.active_light(3):
      lights = []
      if self.settings.light_1:
        lights.append(Light(self.settings.bridge_ip, self.settings.bridge_user, 1))
      if self.settings.light_2:
        lights.append(Light(self.settings.bridge_ip, self.settings.bridge_user, 2))
      if self.settings.light_3:
        lights.append(Light(self.settings.bridge_ip, self.settings.bridge_user, 3))
      self.lights = lights

    return self.lights

def run():
  last = datetime.datetime.now()
  while not xbmc.abortRequested:
    if datetime.datetime.now() - last > datetime.timedelta(seconds=1):
      # check for updates every 1s (fixme: use callback function)
      last = datetime.datetime.now()
      hue.settings.readxml()
    
    player = MyPlayer()
    xbmc.sleep(500)

def state_changed(state):
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
