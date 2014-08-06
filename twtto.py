#coding:utf-8
import twitter
import t_key
import sys

argvs = sys.argv
argc = len(argvs)


consumer_key             = t_key.dict['consumer_key']
consumer_secret          = t_key.dict['consumer_secret']
access_token_key         = t_key.dict['access_token_key']
access_token_secret      = t_key.dict['access_token_secret']

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

if (argc == 1):
    print "What are you doing?: "
    postmsg = sys.stdin.readline()
elif (argc != 2):
    f = open(argvs[1])
    data = "test"
    postmsg = data
    f.close
status = api.PostUpdates(postmsg.decode("utf-8"))
