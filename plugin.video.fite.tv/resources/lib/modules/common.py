'''
	Fite.tv Add-on

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

fanart   = 'special://home/addons/plugin.video.fite.tv/fanart.jpg'
base_img = 'special://home/addons/plugin.video.fite.tv/resources/img/%s.png'

def play(url):
	resolved = url
	item     = xbmcgui.ListItem(path=resolved)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	
def open_url(url):
	req      = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
	response = urllib2.urlopen(req)
	link     = response.read()
	response.close()
	return link
	
def add_link(name,url,mode,iconimage):
	u   = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
	ok  = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	liz.setInfo('video', {'Title': name})
	liz.setProperty("IsPlayable","true")
	ok  = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def add_dir(name,url,mode,iconimage):
	u   = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
	ok  = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	ok  = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	
def get_stream(url):
	link  = open_url(url)
	link  = link.replace('\n','')
	match = re.compile("'video_id':'(.+?)'").findall(link)
	for id in match:
		url   = 'https://www.fite.tv/embed/v1/%s/' % id
		link  = open_url(url)
		link  = link
		match = re.compile('playlist:\[\{sources:\[\{file:"(.+?)"\}\]').findall(link)
		for url in match:
			play(url)