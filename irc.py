import credentials
import irc_commands
import logging
import mssql_commands
import os
import pyodbc
import string
import socket
import subprocess
import sys
import twitch_commands
import wordpress_commands as wordpress
from time import gmtime, strftime

Running = True
channel = credentials.IRC_CHANNEL
server = credentials.IRC_HOST
minutes_modulator = 10

DETACHED_PROCESS = 0x00000008

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


s = socket.socket()
s.connect((server, credentials.IRC_PORT))
s.send("PASS " + credentials.IRC_OAUTH_PASSWORD + "\r\n")
s.send("NICK " + credentials.IRC_NICK + "\r\n")
s.send("JOIN #" + channel + " \r\n")

def Send_message(message):
 s.send("PRIVMSG #" + channel + " :" + message + "\r\n")
 Terminal(message)

def Terminal(message):
 message = message.replace('\n','').replace('\r','').strip()
 print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ": " + message)
     
Send_message("I have returned!")

while(Running):
 try:
  ircmsg = s.recv(1024).strip('\r\n')
  if (ircmsg != ""):
   if (ircmsg.startswith("PING :tmi.twitch.tv")):
    s.send("PONG :tmi.twitch.tv\r\n")
    Terminal(ircmsg)
    Terminal("PONG :tmi.twitch.tv")
   elif((ircmsg.startswith(":tmi.twitch.tv")) or (ircmsg.startswith(":forcethestorm"))):
    for item in ircmsg.split('\n'):
     Terminal(item)
   else:
    username = ircmsg.split("!")[0].split(":")[1]
    message_recieved = ircmsg.split("PRIVMSG #" + channel)[1]
    Terminal("#" + channel + ": " + username + message_recieved)

    #update_last_seen(user, time)

    if (ircmsg.find("PRIVMSG #" + channel + " :!") != -1): 

     if (ircmsg.find(":!card") != -1):
      card = ircmsg.split(":!card ")[1]
      Send_message("@" + username + " " + card + ": " + mssql_commands.Get_Oracle_Text(card))
     
     elif ((ircmsg.find(":!quit") != -1) and (username == channel)):
      os._exit(0)
     
     elif ((ircmsg.find(":!restart") != -1) and (username == channel)):
      subprocess.Popen('python irc.py')
      os._exit(0)
     
     elif ((ircmsg.find(":!uf") != -1) and (username == channel)):         
      #subprocess.Popen(["C:\Python27\Lib\idlelib\idle.pyw", "update_twitch_followers.py"], creationflags=DETACHED_PROCESS)
      os.system('python update_twitch_followers.py')

     elif (ircmsg.find(":!decklists") != -1):
      Send_message(mssql_commands.Get_Decklists())
     
     elif (ircmsg.find(":!deck") != -1):
      deck_name = ircmsg.split(":!deck ")[1]
      Send_message("@" + username + " Deck \"" + deck_name + "\": " + Get_WordPress_Decklist(deck_name))
     
     elif (ircmsg.find(":!article") != -1):
      Send_message("New article up! Check it out at: " + wordpress.Get_Last_Article())
     
     elif (ircmsg.find(":!music") != -1):
      Send_message("Currently playing: " + irc_commands.Get_Music())
     
     elif (ircmsg.find(":!twitter") != -1):
      Send_message("Follow me on Twitter: " + irc_commands.Get_Twitter())
     
     elif (ircmsg.find(":!website") != -1):
      Send_message("Check out the website here! " + irc_commands.Get_Website())
     
     elif (ircmsg.find(":!craig") != -1):
      Send_message("All praise Craig in his majestic glory!")
      #craig = mssql_commands.Get_Total_Craigs()
      #Send_message("Craig has deemed us worthy of his presence ? times", craig)
 except:
  print "Something broke."
