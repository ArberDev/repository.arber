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

def episodes():
	season    = '1'
	episode   = '1'
	title     = 'Pilgrim of Eternity'
	plot      = 'Apollo returns to wreak havoc on the Enterprise in the first episode of the new series.'
	aired     = '2013-05-24'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/4577842.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=66784863'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '2'
	title     = 'Lolani'
	plot      = 'A survivor from a distressed Tellarite vessel pulls Captain Kirk and his crew into a moral quandary over her sovereignty.'
	aired     = '2014-02-08'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/4794512.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=86215323'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '3'
	title     = 'Fairest of Them All'
	plot      = 'In the Mirror Universe, Spock faces a choice that determines the future of the Terran Empire.'
	aired     = '2014-06-15'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/4909034.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=98076892'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '4'
	title     = 'The White Iris'
	plot      = 'Captain Kirk finds himself haunted by guilt from his past as the fate of an alien world hangs in the balance.'
	aired     = '2015-05-29'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/5151398.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=128304406'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '5'
	title     = 'Divided We Stand'
	plot      = 'Kirk and McCoy are trapped in time while an alien infestation threatens the Enterprise.'
	aired     = '2015-09-26'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/5348432.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=139692418'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '6'
	title     = 'Come Not Between the Dragons'
	plot      = 'A troubled creature pierces the Enterprise hull, pitting the crew against a pursuer that threatens to tear them apart.'
	aired     = '2016-05-28'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/5627478.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=165431813'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '7'
	title     = 'Embracing the Winds'
	plot      = 'While the Enterprise is sent on a seemingly routine mission, Kirk is recalled to starbase where he faces an ethical dilemma that challenges the very core of Starfleet Command.'
	aired     = '2016-09-03'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/5731963.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=178685237'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '8'
	title     = 'Still Treads the Shadow'
	plot      = 'The Enterprise discovers a lost starship... with an unlikely passenger.'
	aired     = '2017-04-02'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/6010692.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=210024763'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '9'
	title     = 'What Ships Are For'
	plot      = 'Kirk struggles with aiding a society whose inhabitants view their isolated world in a very unique way.'
	aired     = '2017-07-30'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/6162896.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=226223868'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '10'
	title     = 'To Boldly Go: Part I'
	plot      = 'To solve the ultimate mystery, the Enterprise must return to where Kirk\'s five-year mission began.'
	aired     = '2017-10-18'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/6369613.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=236207052'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	season    = '1'
	episode   = '11'
	title     = 'To Boldly Go: Part II'
	plot      = 'The iconic mission of the U.S.S. Enterprise comes to an end, as Kirk and his crew battle the ultimate adversary.'
	aired     = '2017-11-13'
	thumbnail = 'https://www.thetvdb.com/banners/episodes/264220/6377270.jpg'
	link      = 'plugin://plugin.video.vimeo/play/?video_id=241107969'
	common.addEpisode(title,link,1,thumbnail,season,episode,plot,aired)
	
	xbmcplugin.setContent(int(sys.argv[1]), 'episodes')