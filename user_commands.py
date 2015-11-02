import credentials
import pyodbc
import time

credentials = 'DRIVER={SQL Server};SERVER=' + credentials.SQL_SERVER + \
              ';DATABASE=' + credentials.SQL_DATABASE + \
              ';UID=' + credentials.SQL_USER_ID + \
              ';PWD=' + credentials.SQL_PASSWORD

def add_user(user, 0)
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()
 cursor.execute("SELECT COUNT(twitch_account_id) as CNT FROM Twitch_Users WHERE = ?")
 row = cursor.fetchone()
 if(row.CNT <= 0):
  cursor.execute("INSERT INTO Twitch_Users (twitch_user_account, real_name, Skype, Security_ID, Last_seen) VALUES(?, ?, ?, ?, ?)", level, '', '', user, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
  cursor.commit()
 connection.close
 
def set_level(user, level):
 add_user(user) #add user if not exist
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()
 cursor.execute("UPDATE Twitch_Users SET Security_ID = ? WHERE twitch_user_account = ?", level, user)
 cursor.commit()
 connection.close

def set_regular(user):
 set_level(user, 5)

def ban_user(user):
 set_level(user, -99)

def timeout_user(user):
 set_level(user, -1)
