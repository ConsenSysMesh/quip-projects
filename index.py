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
content = '<h1>Today\'s automated Standup</h1><h2>This document has been added using the Quip API</h2><p>@Doruk Akpek</p><p>@Igor Lilic</p>'


def run():
	# client = quip.QuipClient(access_token="VUZlQU1BN0tZajk=|1516466133|whq6sTaYVldRrNWFs8Nw584tbXpgenX0rJgizoIHvUg=")
	newdocument()
	


def newdocument(format = "html", title = "Testing Stand-Up Automation", member_ids = ["VHPAOAvDhW2"]):
	
	client.new_document(content, member_ids)




run()

