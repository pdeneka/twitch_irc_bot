import credentials
import irc_commands as commands
import mssql_commands
import os
import pyodbc
import string
import socket
import sys
import time
import twitch_commands
import update_twitch_followers as uf
import update_twitch_subscribers as us
import wordpress_commands as wordpress
from time import gmtime, strftime

Running = True
channel = credentials.IRC_CHANNEL
server = credentials.IRC_HOST
seconds_modulator = 45 #how often to scan chat viewer list
minutes_modulator = 10 #how often to scan chat viewer list

s = socket.socket()
s.connect((server, credentials.IRC_PORT))
s.send("PASS " + credentials.IRC_OAUTH_PASSWORD + "\r\n")
s.send("NICK " + credentials.IRC_NICK + "\r\n")
s.send("JOIN #" + channel + " \r\n")

def Send_message(message):
 s.send("PRIVMSG #" + channel + " :" + message + "\r\n")
 print ("PRIVMSG #" + channel + " :" + message + "\r\n")

Send_message("I have returned!")
mssql_commands.Update_Last_Seen('forcethestorm', strftime("%Y-%m-%d %H:%M:%S", gmtime()))

while Running:
 t = time.localtime()
 if((t.tm_sec % seconds_modulator == 0) and (t.tm_min % minutes_modulator == 0)):
  twitch_commands.Check_Viewers()
 ircmsg = s.recv(1024)
 ircmsg = ircmsg.strip('\r\n')
 if (ircmsg != ""):
  if ircmsg.startswith("PING :tmi.twitch.tv"):
   s.send("PONG :tmi.twitch.tv")
   #bot currently times out after 2 pings.
  else:
   try:
    username = ircmsg.split('.tmi.twitch.tv PRIVMSG #freeslagg :')[0].split('@')[1]
    message_recieved = ircmsg.split('.tmi.twitch.tv PRIVMSG #freeslagg :')[1]
    time_received = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    message_to_display = time_received + ": " + username + ": " + message_received
    mssql_commands.Update_Last_Seen(username, time_received)
    print message_to_display.replace('\n','').replace('\n','').replace('\r','').strip()
   except:
    for item in ircmsg.split('\n'):
     print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": " + item
  if ircmsg.find('PRIVMSG #freeslagg :!') != -1:
   #process_chat_command(ircmsg)
   #handle the below
   if ircmsg.find(":!card") != -1:
    card = ircmsg.split(":!card ", 2)[1]
    Send_message(card + ": " + mssql_commands.Get_Oracle_Text(card))
   elif ((ircmsg.find(":!update followers") != -1) and (username == channel)):
    #ONLY WORKS FOR CHANNEL OWNER
    for c in range(0, uf.Get_Follower_Count(channel)+1):
     follower = uf.Get_Follower_Twich_Account_Name(channel, 1, 'DESC', c)
     mssql_commands.Add_Twitch_Follower(username)
   elif ircmsg.find(":!article") != -1:
    msg = "New article up! Check it out at: " + wordpress.Get_Last_Article()
    Send_message(msg)
   elif ircmsg.find(":!music") != -1:
    msg = "Currently playing: " + irc_commands.Get_Music()
    Send_message(msg)
   elif ircmsg.find(":!twitter") != -1:
    msg = "Follow me on Twitter: " + irc_commands.Get_Twitter()
    Send_message(msg)
   elif ircmsg.find(":!website") != -1:
    msg = "Check out the website here! " + irc_commands.Get_Website()
    Send_message(msg)



