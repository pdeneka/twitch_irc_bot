import mssql_credentials as m
import pyodbc

def add_user(user, 0)
 credentials = 'DRIVER={SQL Server};SERVER=' + m.server + ';DATABASE=' + m.database + ';UID=' + m.user_id + ';PWD=' + m.password
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()
 #if user does not exist in table
 #cursor.execute("INSERT INTO Twitch_Users (twitch_user, real_name, Skype, Security_ID, Last_seen)
 # VALUES(?, ?, ?, ?, ?)", level, '', '', user, python.getdatetime())
 cursor.commit()
 connection.close
 
def set_level(user, level):
 add_user(user) #add user if not exist
 credentials = 'DRIVER={SQL Server};SERVER=' + m.server + ';DATABASE=' + m.database + ';UID=' + m.user_id + ';PWD=' + m.password
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
