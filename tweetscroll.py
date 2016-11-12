#!/usr/bin/python3

import sys
import time
import scrollphat

from twython import TwythonStreamer

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

scrollphat.clear()
scrollphat.set_brightness(4)
scrollphat.set_rotate(True)

# Sleep for a bit to let WiFi connect
time.sleep(30)

class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			username = data['user']['screen_name']
			tweet = data['text']
			message = "@%s: %s" % (username, tweet)
			scroll_tweet(message.upper())

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def scroll_tweet(message):
    status = '     >>>>>     ' + message + '     <<<<<     '
    status = status.encode('ascii', 'ignore').decode('ascii')
    scrollphat.write_string(status)
    status_length = scrollphat.buffer_len()
    while status_length > 0:
        scrollphat.scroll()
        time.sleep(0.1)
        status_length -= 1

stream.statuses.filter(track='<SEARCH TERM HERE>')
