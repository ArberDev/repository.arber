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

import common
import json
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

base_url = 'https://www.fite.tv/replays/%s/#schedule'
base_img = 'special://home/addons/plugin.video.fite.tv/icon.png'

def main():
	common.add_dir('MMA',base_url % 'mma',2,base_img)
	common.add_dir('Wrestling',base_url % 'wrestling',2,base_img)
	common.add_dir('Boxing',base_url % 'boxing',2,base_img)
	common.add_dir('Kickboxing',base_url % 'muay-thai-kickboxing',2,base_img)
	common.add_dir('Traditional',base_url % 'traditional-martial-arts',2,base_img)
		
def replays(url):
	items = []
	link  = common.open_url(url)
	link  = link.replace('\n','')
	match = re.compile('<script type="application/ld\+json">(.+?)</script>').findall(link)
	for data in match: 
		if 'location' not in data:
			pass
		else:
			data = str(data)
			data = json.loads(data)
			for i in data:
				try: url = i['offers']['url']
				except: pass

				try: date = i['offers']['validFrom'][:10]
				except: pass
				
				try: price = i['offers']['price']
				except: pass
				
				try: img = i['image']
				except: pass
				
				try: title = i['name']
				except: pass
				
				if url not in items:
					items.append(url)
					title = '[B]%s[/B] | %s' % (date, title)
					if price == '0':
						common.add_link(title,url,1,img)
					else:
						pass
				else:
					pass
	
	more = re.compile('<div class="show-more"><a href="(.+?)">Show more').findall(link)
	for url in more:
		img   = base_img
		title = '[I]More...[/I]'
		url   = 'https://www.fite.tv%s' % url
		common.add_dir(title,url,2,img)
		
