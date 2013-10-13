#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import sys
import time
import imp
from random import choice


pylast = imp.load_source('pylast', 'libs/pylast.py')
songs = imp.load_source('songs', 'libs/songs.py')

API_KEY = "55a3efd55018c6023197280946f578a2";
API_SECRET = "1a9530bd9d522eef14e40d47a00024cf"
USERNAME = "hasantayyar"
PASSWORD = "123450"
THRESHOLD = 50
artist = "Pink Floyd"
title = choice(songs.allsongs).replace(".mp3","")
song_started = str(time.time()).split('.')[0]

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = USERNAME, password_hash = pylast.md5(PASSWORD))
network.scrobble(artist = artist, title = title, timestamp = song_started)
print(title + " " + song_started)

#logging.debug("#############",song_started)
