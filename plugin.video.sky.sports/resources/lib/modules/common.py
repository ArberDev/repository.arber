'''
	Sky Sports News Add-on

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

fanart   = 'special://home/addons/plugin.video.sky.sports/fanart.jpg'
base_img = 'special://home/addons/plugin.video.sky.sports/resources/img/%s.png'

get_quality = xbmcaddon.Addon('plugin.video.sky.sports').getSetting('quality')
if get_quality == '0': quality = '3600'
if get_quality == '1': quality = '2200'
if get_quality == '2': quality = '600'
if get_quality == '3': quality = '300'

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
		
def browse(url):
	link  = open_url(url)
	link  = link
	match = re.compile('data-src="(.+?)/384x216/(.+?)\.jpg.+?"\n                alt="(.+?)"').findall(link)
	for img,vid_id,title in match:
		title = title.replace('&#8211;','-')
		title = title.replace('&#8217;','\'')
		title = title.replace('&#8216;','\'')
		img   = img + '/1920x1080/' + vid_id + '.jpg'
		url   = 'http://player.ooyala.com/hls/player/all/' + vid_id + '/media/' + quality + '.m3u8'
		add_link(title,url,2,img)
		
	more = re.compile('href="/watch/video/sports/(.+?)/more/(.+?)"').findall(link)
	for sport,url in more:
		url   = 'http://www.skysports.com/watch/video/sports/' + sport + '/more/' + url
		title = '[I]More...[/I]'
		img   = base_img % 'more'
		add_dir(title,url,1,img)