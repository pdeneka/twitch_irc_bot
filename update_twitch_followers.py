import credentials
import json
import mssql_commands
import pprint
import requests

#See instructions here:
#https://github.com/justintv/Twitch-API/blob/
# master/v3_resources/follows.md#get-channelschannelfollows

Access_Token = credentials.API_ACCESS_TOKEN
Client_ID = credentials.API_CLIENT_ID
Channel = credentials.TWITCH_CHANNEL

Direction = 'DESC' #or ASC
Limit = "1"
Offset = "0"
DEBUG = credentials.DEBUG

r = requests.get('https://api.twitch.tv/kraken/channels/' + Channel + \
                 '/follows?direction=' + Direction + '&limit=' + Limit + \
                 '&offset=' + Offset + ', auth=(Client_ID,Access_Token)')

def my_safe_repr(object, context, maxlevels, level):
    typ = pprint._type(object)
    if typ is unicode:
        object = str(object)
    return pprint._safe_repr(object, context, maxlevels, level)

printer = pprint.PrettyPrinter()
printer.format = my_safe_repr
pp = pprint.PrettyPrinter(depth=20)

total_followers = r.json()['_total']

def Output(msg):
 output = '* ' + msg
 length = 59 - len(output)
 for i in range(0,length):
  output = output + ' '
 output = output + '*'
 return output

def Get_Follower_Count(Channel):
 r = requests.get('https://api.twitch.tv/kraken/channels/' + Channel + \
                 '/follows?direction=' + Direction + '&limit=' + str(Limit) + \
                 '&offset=' + str(Offset) + ', auth=(Client_ID,Access_Token)')
 total_followers = r.json()['_total']
 return total_followers

def Get_Follower_Twich_Account_Name(Channel, Limit, Direction, Page_Offset):
 r = requests.get('https://api.twitch.tv/kraken/channels/' + Channel + \
                 '/follows?direction=' + Direction + '&limit=' + str(Limit) + \
                 '&offset=' + str(Page_Offset - 1) + ', auth=(Client_ID,Access_Token)')

 data = json.dumps(r.json())
 user = data.split('https://api.twitch.tv/kraken/users/')[1]
 user = user.split('/follows/channels/' + Channel)[0]

 if(DEBUG):
  print '************************************************************'
  print Output('Status Code: ' + str(r.status_code))
  print Output('Headers:     ' + r.headers['content-type'])
  print Output('Encoding:    ' + r.encoding)
  print Output('Followers:   ' + str(total_followers))
  print Output('User #:      ' + str(Page_Offset))
  print Output('Account:     ' + str(user))
  print '************************************************************'

 return user

def Confirm_Account_Following(Channel):
 print 'Confirm_Account_Following(Channel) Not yet implemented'

for c in range(Get_Follower_Count(Channel)+1, 0):
 follower = Get_Follower_Twich_Account_Name(Channel, 1, 'DESC', c)
 found = mssql_commands.Add_Twitch_Follower(follower)
 if(found==True):
  break
  
