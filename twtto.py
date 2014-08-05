#coding:utf-8
import twitter
import sys


consumer_key             = ''
consumer_secret          = ''
access_token_key         = ''
access_token_secret      = ''

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

print "What are you doing?:"
postmsg = sys.stdin.readline()

status = api.PostUpdates(postmsg.decode("utf-8"))
