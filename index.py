import datetime
import json
import logging
import sys
import time
import urllib
import urllib2
import quip

reload(sys)
sys.setdefaultencoding('utf8')

client = quip.QuipClient(access_token="VUZlQU1BN0tZajk=|1516466133|whq6sTaYVldRrNWFs8Nw584tbXpgenX0rJgizoIHvUg=")

def run():
	# client = quip.QuipClient(access_token="VUZlQU1BN0tZajk=|1516466133|whq6sTaYVldRrNWFs8Nw584tbXpgenX0rJgizoIHvUg=")
	
	newdocument()


def newdocument():
	client.new_document("<h1>Hello World</h1><p>Let's see if this works</p>")


run()
