import credentials
import mssql_commands
import pyodbc
import urllib2


#future problems:
#Account for 4 digits worth of viewers in Get_Chatter_Count
# Hopefully it does not use commas...

url = "https://tmi.twitch.tv/group/user/" + credentials.TWITCH_CHANNEL + "/chatters"

CREDENTIALS = 'DRIVER={SQL Server};SERVER=' + credentials.SQL_SERVER + \
              ';DATABASE=' + credentials.SQL_DATABASE + \
              ';UID=' + credentials.SQL_USER_ID + \
              ';PWD=' + credentials.SQL_PASSWORD

def Update_Chat_Roster(twitch_chat_username, twitch_chat_user_level):
 mssql_commands.Add_User(twitch_chat_username)
 print "New user present: " + twitch_chat_username
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute('\
     UPDATE a \
	SET a.twitch_chat_user_level = tcl.id \
    FROM tie_Twitch_User_Twitch_Chat AS a \
    LEFT JOIN Twitch_Chat_Levels AS tcl ON tcl.Short = ? \
    LEFT JOIN Twitch_Users AS u ON a.twitch_user_id = u.id \
    WHERE LOWER(u.twitch_user_account) = ?', twitch_chat_user_level.lower(), twitch_chat_username.lower())
 cursor.commit()
 connection.close
 
def Check_Viewers():
 webpage_opener = urllib2.urlopen(url)
 webpage = webpage_opener.read()
 Get_Chatter_Count(webpage)
 Get_Moderators(webpage)
 Get_Staff(webpage)
 Get_Admins(webpage)
 Get_Global_Mods(webpage)
 Get_Viewers(webpage)

def Get_Chatter_Count(webpage):
 chatter_count = webpage.split('"chatter_count": ')[1]
 chatter_count = chatter_count.split(',')[0]

def Get_Moderators(webpage):
 moderators = webpage.split('"moderators": [')[1]
 moderators = moderators.split('],')[0]
 moderators = moderators.strip()
 for m in moderators.split('\n'):
  moderator = m.replace('"', '').replace(',', '').strip()
  if(moderator != ""):
   Update_Chat_Roster(moderator, "Moderator")
  

def Get_Staff(webpage):
 staffs = webpage.split('"staff": [')[1]
 staffs = staffs.split(']')[0]
 staffs = staffs.strip()
 for staff in staffs.split('\n'):
  staff = staff.replace('"', '').replace(',', '').strip()
  if(staff != ""):
   Update_Chat_Roster(staff, "Staff")

def Get_Admins(webpage):
 admins = webpage.split('"admins": [')[1]
 admins = admins.split(']')[0]
 admins = admins.strip()
 for a in admins.split('\n'):
  admin = a.replace('"', '').replace(',', '').strip()
  if(admin != ""):
   Update_Chat_Roster(admin, "Admin")
 
def Get_Global_Mods(webpage):
 global_mods = webpage.split('"global_mods": [')[1]
 global_mods = global_mods.split(']')[0]
 global_mods = global_mods.strip()
 for global_mod in global_mods.split('\n'):
  global_mod = global_mod.replace('"', '').replace(',', '').strip()
  if(global_mod != ""):
   Update_Chat_Roster(global_mod, "Global Moderator")

def Get_Viewers(webpage):
 viewers = webpage.split('"viewers": [')[1]
 viewers = viewers.split(']')[0]
 viewers = viewers.strip()
 for viewer in viewers.split('\n'):
  viewer = viewer.replace('"', '').replace(',', '').strip()
  if(viewer != ""):
   Update_Chat_Roster(viewer, "Viewer")


def Get_Subscribers():
 print "twitch_commands.Get_Subscribers() is not yet implemented."
