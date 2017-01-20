import datetime
import json
import logging
import sys
import time
import urllib
import urllib2


reload(sys)
sys.setdefaultencoding('utf8')

def run():
	client = quip.QuipClient("VUZlQU1BN0tZajk=|1516466133|whq6sTaYVldRrNWFs8Nw584tbXpgenX0rJgizoIHvUg=")
	
	newdocument()


def newdocument():
	client.new_document("<h1>Hello World</h1><p>Let's see if this works</p>")


run()
