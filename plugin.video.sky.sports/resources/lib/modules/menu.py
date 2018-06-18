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

import common
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

base_url     = 'http://www.skysports.com/watch/video/sports/%s'
featured_url = 'http://www.skysports.com/watch/video'
base_img     = 'special://home/addons/plugin.video.sky.sports/icon.png'

def main():
	common.add_dir( 'Featured',     featured_url,              1, base_img )
	common.add_dir( 'Football',     base_url % 'football',     1, base_img )
	common.add_dir( 'F1',           base_url % 'f1',           1, base_img )
	common.add_dir( 'Cricket',      base_url % 'cricket',      1, base_img )
	common.add_dir( 'Rugby Union',  base_url % 'rugby-union',  1, base_img )
	common.add_dir( 'Rugby League', base_url % 'rugby-league', 1, base_img )
	common.add_dir( 'Golf',         base_url % 'golf',         1, base_img )
	common.add_dir( 'Boxing',       base_url % 'boxing',       1, base_img )
	common.add_dir( 'NFL',          base_url % 'nfl',          1, base_img )
	common.add_dir( 'Darts',        base_url % 'darts',        1, base_img )
	common.add_dir( 'Racing',       base_url % 'racing',       1, base_img )
	common.add_dir( 'Cycling',      base_url % 'cycling',      1, base_img )
	common.add_dir( 'Snooker',      base_url % 'snooker',      1, base_img )
	common.add_dir( 'Equestrian',   base_url % 'equestrian',   1, base_img )
	common.add_dir( 'WWE',          base_url % 'wwe',          1, base_img )
	common.add_dir( 'UFC',          base_url % 'ufc',          1, base_img )
	common.add_dir( 'Netball',      base_url % 'netball',      1, base_img )
	