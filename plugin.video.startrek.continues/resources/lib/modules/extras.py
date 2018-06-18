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

def extras():
	title     = 'Set Walk-Thru'
	thumbnail = 'https://www.startrekcontinues.com/images/bts8.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=99949971'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 1 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts11.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=137546232'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 2 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts24.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=235687587'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 3 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts4a.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=98616461'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 3 Surprise!'
	thumbnail = 'https://www.startrekcontinues.com/images/bts3.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=99377574'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Behind the Mirror (Part 1)'
	thumbnail = 'https://www.startrekcontinues.com/images/bts7.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=99377575'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Behind the Mirror (Part 2)'
	thumbnail = 'https://www.startrekcontinues.com/images/bts6.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=99377577'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Behind the Mirror (Part 3)'
	thumbnail = 'https://www.startrekcontinues.com/images/bts5.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=99377576'
	common.addLink(title,link,1,thumbnail)
	
	title     = '2015 "Kirk" Starter Campaign'
	thumbnail = 'https://www.startrekcontinues.com/images/bts25.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=241104231'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 4 Scoring'
	thumbnail = 'https://www.startrekcontinues.com/images/bts10.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=131927987'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 4 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts9.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=128463799'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 5 Scoring'
	thumbnail = 'https://www.startrekcontinues.com/images/bts13.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=139671876'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 5 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts12.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=139671877'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Our Crew: Ralph M. Miller'
	thumbnail = 'https://www.startrekcontinues.com/images/bts14.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=156658638'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Our Crew: Greg Dykstra'
	thumbnail = 'https://www.startrekcontinues.com/images/bts16.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=167874809'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 6 Scoring'
	thumbnail = 'https://www.startrekcontinues.com/images/bts18.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=167876913'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 6 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts17.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=166340512'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 6 Redshirt Gag'
	thumbnail = 'https://www.startrekcontinues.com/images/bts20.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=180701834'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 7 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts21.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=181371790'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 8 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts22.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=210870918'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 9 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts23.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=224920620'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Our Crew: Vic Mignogna'
	thumbnail = 'https://www.startrekcontinues.com/images/bts26.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=241132583'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 10 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts30.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=243477836'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Our Crew: Marc Bell'
	thumbnail = 'https://www.startrekcontinues.com/images/bts27.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=242664077'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 11 Scoring'
	thumbnail = 'https://www.startrekcontinues.com/images/bts28.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=242665055'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Episode 11 Gag Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts31.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=245493651'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'That\'s a Wrap'
	thumbnail = 'https://www.startrekcontinues.com/images/bts32.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=245561219'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'The Final Goodbye'
	thumbnail = 'https://www.startrekcontinues.com/images/bts29.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=243398547'
	common.addLink(title,link,1,thumbnail)
	
	title     = 'Teaser Reel'
	thumbnail = 'https://www.startrekcontinues.com/images/bts15.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=160566634'
	common.addLink(title,link,1,thumbnail)
	
	