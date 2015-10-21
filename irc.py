import irc_commands as cmd
import irc_credentials as c
import mssql_credentials as m
import os
import pyodbc
import string
import socket
import sys
from time import gmtime, strftime

Running = True
channel = c.CHAN
server = c.HOST

s = socket.socket()
s.connect((server, c.PORT))
s.send("PASS " + c.PASS + "\r\n")
s.send("NICK " + c.NICK + "\r\n")
s.send("JOIN #" + channel + " \r\n")

def Send_message(message):
 s.send("PRIVMSG #freeslagg :" + message + "\r\n")
 print ("PRIVMSG #freeslagg :" + message + "\r\n")

def ping():
 s.send(server + ": PONG")
 print(server + ": PONG")

def get_oracle_text(card):
 credentials = 'DRIVER={SQL Server};SERVER=' + m.server + ';DATABASE=' + m.database + ';UID=' + m.user_id + ';PWD=' + m.password
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()
 cursor.execute("SELECT Oracle_Text FROM python_Oracle WHERE lower(Card_Name) = ?", card)
 rows = cursor.fetchall()
 connection.close
 oracle_text = ""
 for row in rows:
  oracle_text = row[0]
 return oracle_text.replace('\n', ' ')

def add_quote(user, quote):
 credentials = 'DRIVER={SQL Server};SERVER=' + m.server + ';DATABASE=' + m.database + ';UID=' + m.user_id + ';PWD=' + m.password
 t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()
 cursor.execute("INSERT INTO QUOTE(twitch_user_account_id, quote, date_added", user, quote, t)
 cursor.commit()
 connection.close


Send_message("I have returned!")

#servername / ( nickname [ [ "!" user ] "@" host ] )
#:user!user@user.tmi.twitch.tv PRIVMSG #channel :msg

while Running:
 ircmsg = s.recv(1024)
 ircmsg = ircmsg.strip('\r\n')
 if (ircmsg != ""):
  print(ircmsg)
  if ircmsg.find("PING :tmi.twitch.tv") != -1:
   ping()
  elif ircmsg.find('PRIVMSG #freeslagg :!') != -1:
   if ircmsg.find(":!card") != -1:
    card = ircmsg.split(":!card ", 2)[1]
    Send_message(card + ": " + get_oracle_text(card))
   elif ircmsg.find(":!addquote"):
    quote = ircmsg.split(":!addquote ", 2)[1]
    user = ircmsg.split("!", 2)[0]
    user = user.replace(":", "")
    add_quote(user, quote)
