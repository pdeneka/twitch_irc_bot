import credentials
import json
import mssql_commands
import pprint
import requests

Access_Token = credentials.API_ACCESS_TOKEN
Client_ID = credentials.API_CLIENT_ID
Channel = credentials.TWITCH_CHANNEL

chat_url = "https://tmi.twitch.tv/group/user/" + Channel + "/chatters"

c = requests.get(chat_url)

def my_safe_repr(object, context, maxlevels, level):
    typ = pprint._type(object)
    if typ is unicode:
        object = str(object)
    return pprint._safe_repr(object, context, maxlevels, level)

printer = pprint.PrettyPrinter()
printer.format = my_safe_repr
pp = pprint.PrettyPrinter(depth=20)

status_code = c.status_code
headers = c.headers['content-type']
encoding = c.encoding

print "Status Code: " + str(status_code)
print "Headers: " + str(headers)
print "Encoding: " + str(encoding)
print("JSON")
try:
 pp.pprint(c.json())
except:
 print "No JSON available."

print "Chatter Count: " + str(c.json()['chatter_count'])
print "Links: " + str(c.json()['_links'])
print "Chatters: " + str(c.json()['chatters'])

print "Admins: " + str(c.json()['admins'])
print "global_mods: " + str(c.json()['global_mods'])
print "moderators: " + str(c.json()['moderators'])
print "viewers: " + str(c.json()['viewers'])





















sample_json = "{u'_links': {}, \
 u'chatter_count': 5, \
 u'chatters': {u'admins': [], \
               u'global_mods': [], \
               u'moderators': [u'creaturemystery', u'freeslagg'], \
               u'staff': [], \
               u'viewers': [u'jennyisawesome', u'obsidianstee1', u'wurth86']}} \
{ \
  \"_links\": {}, \
  \"chatter_count\": 5, \
  \"chatters\": { \
    \"moderators\": [ \
      \"creaturemystery\", \
      \"freeslagg\" \
    ], \
    \"staff\": [], \
    \"admins\": [], \
    \"global_mods\": [], \
    \"viewers\": [ \
      \"jennyisawesome\", \
      \"obsidianstee1\", \
      \"wurth86\" \
    ] \
  } \
}"
