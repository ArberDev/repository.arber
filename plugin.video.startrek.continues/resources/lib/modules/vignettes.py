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

import base64
import common
import urllib
import urllib2
import re
import xbmcplugin
import xbmcgui
import os
import sys
import datetime
import string
import xbmc
import xbmcaddon

fanart = 'special://home/addons/plugin.video.startrek.continues/fanart.jpg'

def vignettes():
	title     = 'Vignette 1: Turnabout Intruder'
	thumbnail = 'https://www.startrekcontinues.com/images/vignette1.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=46712562'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Vignette 2: You\'ve Got The Conn'
	thumbnail = 'https://www.startrekcontinues.com/images/vignette2.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=50482363'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Vignette 3: Happy Birthday, Scotty'
	thumbnail = 'https://www.startrekcontinues.com/images/vignette3.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=54562820'
	common.addLink(title,link,1,thumbnail)
	
	