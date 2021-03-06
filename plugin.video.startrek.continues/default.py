'''
	Star Trek Continues Add-on
	Copyright (C) 2018 Arber

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import hashlib
import os
import re
import string
import sys
import urllib
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs
from resources.lib.modules.common import *
from resources.lib.modules.episodes import *
from resources.lib.modules.extras import *
from resources.lib.modules.library import *
from resources.lib.modules.vignettes import *

icon   = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.startrek.continues', 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.startrek.continues', 'fanart.jpg'))

def main():
	addDir('Watch Episodes','url',2,icon)
	addDir('Watch Extras','url',5,icon)
	addDir('Watch Vignettes','url',4,icon)
	addImport('Import to Library','url',3,icon)
		
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
              
params = get_params()
url  = None
name = None
mode = None

try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass

print "Mode: "+str(mode)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
	print ""
	main()
	
elif mode==1: play(url)
elif mode==2: episodes()
elif mode==3: libImport()
elif mode==4: vignettes()
elif mode==5: extras()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
