import credentials
import pyodbc
from time import gmtime, strftime

#Todo:
#timeout_user
#set_regular
#interface Ban & Timeout w/ Twitch so bot commands affect Twitch Users

CREDENTIALS = 'DRIVER={SQL Server};SERVER=' + credentials.SQL_SERVER + ';DATABASE=' + credentials.SQL_DATABASE + ';UID=' + credentials.SQL_USER_ID + ';PWD=' + credentials.SQL_PASSWORD

#Card Commands
def Get_Oracle_Text(card):
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute("SELECT Oracle_Text FROM python_Oracle WHERE lower(Card_Name) = ?", card)
 row = cursor.fetchone()
 connection.close
 return row.Oracle_Text

#User Commands
def Add_User(user):
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute("SELECT count(*) AS cnt FROM Twitch_Users WHERE twitch_user_account = ?", user)
 row = cursor.fetchone()
 if(row.cnt < 1):
  cursor.execute("INSERT INTO Twitch_Users (twitch_user_account) VALUES(?)", user)
  cursor.commit()
  cursor.execute("SELECT count(*) AS cnt FROM Twitch_Users WHERE twitch_user_account = ?", user)
  row = cursor.fetchone()
  if(row.cnt == 1):
   print "Added user: ", user
  else:
   print "User " + user + " already exists."
 connection.close

def Add_Twitch_Follower(user):
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute("SELECT count(*) AS cnt FROM Twitch_Users WHERE twitch_user_account = ?", user)
 row = cursor.fetchone()
 if(row.cnt < 1):
  cursor.execute("INSERT INTO Twitch_Users (twitch_user_account, real_name, Skype, Security_ID, Last_Seen) VALUES (?, "", "", 1, GETTIME())", user)
  cursor.commit()
  cursor.close()
  print "Added user: " + user
 else:
  print "User " + user + " already exists."

def Get_Twitch_User_ID(user):
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute("SELECT COALESCE(id, -500) FROM Twitch_Users WHERE twitch_user_account = ?", user)
 row = cursor.fetchone()
 connection.close
 return row.id
 #if not exist, add to database
 #if(row.id == -500):
  #Add_User(user)

def Revoke_Privileges(user_making_request, target_user):
 Get_User_Security_Level(user_making_request)
 if(row.Security_ID >= 100):
  Update_User_Level(user_making_request, target_user, -1)

def Ban_User(user_making_request, target_user):
 Get_User_Security_Level(user_making_request)
 if(row.Security_ID >= 100):
  Update_User_Level(user_making_request, target_user, -99)
 print "Add Twitch channel ban functionality"
 #Todo http://www.twitch.tv/freeslagg/chat?popout=
                
def Get_User_Security_Level(user):
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute("SELECT Security_ID FROM Twitch_Users WHERE twitch_user_account = ?", user)
 row = cursor.fetchone()
 connection.close
 return row.Security_ID

def Update_User_Level(user_making_request, target_user, target_user_new_security_level):
 access_granted = false
 Get_User_Security_Level(user_making_request)
 if(row.Security_ID >= 500): #bot OP access
  access_granted = true
 elif((rows.Security_ID >= 100) and (target_user_new_security_level < 100)):
  access_granted = true
 if(access_granted):
  connection = pyodbc.connect(CREDENTIALS)
  cursor = connection.cursor()
  cursor.execute("UPDATE Twitch_Users SET Security_ID = ? WHERE id = ?", target_user_new_security_level, target_user)
  cursor.commit()
  connection.close
  if(Get_User_Security_Level(target_user) == target_user_new_security_level):
   print "Security level updated for user " + target_user + "."
   print "New security level is " + target_user_new_security_level + "."
  else:
   print "Failed to update security level for user " + target_user + " to level " + target_user_new_security_level + "."
 else:
  print "Unauthorized user \"" + user_making_request + "\" requested to give user \"" + target_user + "\" security level " + target_user_new_security_level + "."
 

def Update_Last_Seen(user, time):
 connection = pyodbc.connect(CREDENTIALS)
 cursor = connection.cursor()
 cursor.execute("UPDATE Twitch_Users SET Last_Seen = ? WHERE twitch_user_account = ?", time, user)
 cursor.commit()
 connection.close
