'''
	Box Plus Network Add-on
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

import re
import utils
import xbmcaddon

bpn    = xbmcaddon.Addon('plugin.video.boxplus')
lines  = bpn.getSetting('lines')
icon   = 'special://home/addons/plugin.video.boxplus/resources/artwork/%s.png'
fanart = 'special://home/addons/plugin.video.boxplus/fanart.jpg'

def build_channels():
	url   = utils.open_url('https://www.boxplus.com')
	match = re.compile('<p><a href = "https://www\.boxplus\.com/live-tv-guide\?channel=(.+?)">(.+?)</a></p></td></tr>').findall(url)
	for url, show in match:
		name = url.replace('-',' ')
		name = name.title()
		if lines == 'false': name = '[B]%s[/B] - %s' % (name, show)
		else: name = '[B]%s[CR]NOW:[/B] %s' % (name, show)
		utils.add_stream(name, url, 'play', icon % url)
		
def get_stream(url):
	url   = utils.open_url('https://www.boxplus.com/live-tv-guide?channel=' + url)
	match = re.compile("src: '(.+?)',").findall(url)
	for url in match:
		utils.play_stream(url)