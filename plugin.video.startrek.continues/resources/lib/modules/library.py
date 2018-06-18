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

import common
import os
import re
import sys
import string
import urllib
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs

def libImport():
	ret = xbmcgui.Dialog().yesno('Library Import', 'Are you sure you want to create .strm files for this show?')
	if ret:
	
		addon_id      = xbmcaddon.Addon().getAddonInfo('id')
		selfAddon     = xbmcaddon.Addon(id=addon_id)
		libraryFolder = selfAddon.getSetting('library.folder')
		loc           = xbmc.translatePath(os.path.join(libraryFolder, 'Star Trek Continues'))
		xbmcvfs.mkdir(loc)
		
		file = os.path.join(loc,'Star Trek Continues S01E01.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=66784863')
		f.close()
		
		file = os.path.join(loc,'Star Trek Continues S01E02.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=86215323')
		f.close()
		
		file = os.path.join(loc,'Star Trek Continues S01E03.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=98076892')
		f.close()
		
		file = os.path.join(loc,'Star Trek Continues S01E04.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=128304406')
		f.close()
		
		file = os.path.join(loc,'Star Trek Continues S01E05.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=139692418')
		f.close()
	
		file = os.path.join(loc,'Star Trek Continues S01E06.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=165431813')
		f.close()
	
		file = os.path.join(loc,'Star Trek Continues S01E07.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=178685237')
		f.close()
	
		file = os.path.join(loc,'Star Trek Continues S01E08.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=210024763')
		f.close()
	
		file = os.path.join(loc,'Star Trek Continues S01E09.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=226223868')
		f.close()
	
		file = os.path.join(loc,'Star Trek Continues S01E10.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=236207052')
		f.close()
	
		file = os.path.join(loc,'Star Trek Continues S01E11.strm')
		f = xbmcvfs.File(file,'wb')
		f.write('plugin://plugin.video.vimeo/play/?video_id=241107969')
		f.close()
		
		xbmcgui.Dialog().ok('Library Import', 'Library import is complete.')