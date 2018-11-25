'''
	The FunkStation Add-on
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

import utils
import xbmcaddon

bpn    = xbmcaddon.Addon('plugin.audio.funkstation')
radio  = 'http://listento.thefunkstation.com:8000/'
icon   = 'special://home/addons/plugin.audio.funkstation/icon.png'
fanart = 'special://home/addons/plugin.audio.funkstation/fanart.jpg'

def menu():
	utils.add_stream('Listen to The FunkStation', radio, 'play', icon)
		
def get_stream(url):
	utils.play_stream(url)