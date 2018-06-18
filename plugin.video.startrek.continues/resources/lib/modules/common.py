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

fanart	= 'special://home/addons/plugin.video.startrek.continues/fanart.jpg'

def play(url):
	resolved = url
	item	 = xbmcgui.ListItem(path=resolved)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	
def open_url(url):
	req	  = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
	response = urllib2.urlopen(req)
	link	 = response.read()
	link	 = cleanHex(link)
	response.close()
	return link
	
def addEpisode(name,url,mode,thumb,season,episode,plot,aired):
	u   = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok  = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumb)
	liz.setInfo(type='Video', infoLabels={'TVShowTitle':'Star Trek Continues', 'Season':season, 'Episode':episode, 'Premiered':aired, 'Plot':plot, 'Title':name, 'Duration':'3000','Genre':'Science-Fiction','Studio':'YouTube'})
	liz.setArt({'thumb': thumb, 'poster': 'https://www.thetvdb.com/banners/posters/264220-4.jpg', 'banner': 'https://www.thetvdb.com/banners/graphical/264220-g4.jpg'})
	liz.setProperty("IsPlayable","true")
	ok  = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addLink(name,url,mode,iconimage):
	u   = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok  = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setProperty("IsPlayable","true")
	ok  = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addDir(name,url,mode,iconimage):
	u   = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok  = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', iconimage)
	ok  = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def addImport(name,url,mode,iconimage):
		u   = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
		ok  = True
		liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setProperty('fanart_image', iconimage)
		ok  = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
		return ok
	
def cleanHex(text):
	def fixup(m):
		text = m.group(0)
		if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
		else: return unichr(int(text[2:-1])).encode('utf-8')
	try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
	except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
