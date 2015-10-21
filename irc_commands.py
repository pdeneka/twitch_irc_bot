import pyodbc
import mssql_credentials

#placeholder
ircmsg = ''

def Send_message(message):
 s.send("PRIVMSG #freeslagg :" + message + "\r\n")
 print ("PRIVMSG #freeslagg :" + message + "\r\n")

def ping():
 s.send(server + ": PONG")
 print(server + ": PONG")
 
def get_user_level(ircmsg):
 user = ircmsg.split(":!regular ", 2)[0]
 credentials = 'DRIVER={SQL Server};SERVER=' + m.server + ';DATABASE=' + m.database + ';UID=' + m.user_id + ';PWD=' + m.password
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()
 cursor.execute("SELECT Security_ID FROM Twitch_Users WHERE twitch_user_account = ?", user)
 rows = cursor.fetchall()
 connection.close
 twitch_user_security_level = ""
 for row in rows:
  twitch_user_security_level = row[0]
 return twitch_user_security_level.replace('\n', ' ')

#def Craig(action_int):
 #if action_int >= 1:
  #INSERT Twitch_Counters ('Craig', datetime())
 #if action_int <= -1
  #
 #SELECT COUNT(Craig)
 #return count

#ARTICLE
#on 100 & Contributor, set article
#on 1:TEXT:!article: { http://www.forcethestorm.com/index.php/2015/10/13/quick-update/ }

#CARD card_name
if (ircmsg.find(":!card") != -1):
 c = ircmsg.split(":!card ", 2)[1]
 Send_message(c + ": " + get_oracle_text(c))

#COMMANDS
if (ircmsg.find(":!commands") != -1 or ircmsg.find(":!help") != -1):
 Send_message("Commands available: !card card name")

#CRAIG
if (ircmsg.find(":!craig") != -1):
 Send_message("Craig is not yet implemented.")
 #split on !craig
 #get number
 #craig_number = !craig \d*
 #if (get_user_level(ircmsg) = 100):
  #craig_counter = Craig(craig_input)
 #elif (get_user_level(ircmsg) = 1):
  #craig_counter = Craig(0)
#on 100:TEXT:!craig:: { inc %Craig 1 | msg $chan Craig added!  Craig has jumped in front of the screen %Craig times. }
#on 1:TEXT:!craig:: { msg $chan Craig has jumped in front of the screen %Craig times. }
#on 100:TEXT:!remove_craig:: { dec %Craig 1 | msg $chan Craig removed! Craig has jumped in front of the screen %Craig times. }

#DAILYMOTION 
#!dailymotion - http://www.dailymotion.com/Forcing_The_Storm

#DECK
if (ircmsg.find(":!deck") != -1):
 Send_message("!deck is not yet implemented.")

#FACEBOOK
if ((ircmsg.find(":!fb") != -1) or (ircmsg.find(":!facebook") != -1)):
 Send_message("Facebook: https://www.facebook.com/pages/Forcing-The-Storm/1541746969430536?ref=hl")

#HELP
if (ircmsg.find(":!help") != -1):
 Send_message("Sorry, !help is not functional yet.  Check back soon!")
 #!rules !info !list !deck !twitter

#MUSIC
if (ircmsg.find(":!music") != -1):
 Send_message("Sorry, !music is not functional yet.  Check back soon!")
 #read from c:\unp\unp_now_playing.txt
 #ignore first two characters (music note, space)

#PUNS
if (ircmsg.find(":!puns") != -1):
 Send_message("Sorry, !puns is not functional yet.  Check back soon!")
 #on 100:TEXT:!puns:: { inc %puns 1 | msg $chan Pun added!  Total puns to date: %puns }
 #on 100:TEXT:!remove_pun:: { dec %puns 1 | msg $chan Pun removed!  Total puns to date: %puns }
 #on 1:TEXT:!puns:: { msg $chan Puns: %puns }

#PUNT
if (ircmsg.find(":!punt") != -1):
 Send_message("Sorry, !punt is not functional yet.  Check back soon!")
 #on 100:TEXT:!punt: { inc %punt 1 | msg $chan Punt added!  Total punts to date: %punt }
 #on 1:TEXT:!punt:: { msg $chan Punts: %punt }

#QUOTES
if (ircmsg.find(":!addquote") != -1):
 Send_message("Sorry, !addquote is not functional yet.  Check back soon!")
 #add quote (submitter, quote)
  #initiate confirm vote
   #on 2 votes, set quote active
 #remove quote (set active = 0)

#SECURITY (Bot, Website, Channel?)
if (ircmsg.find(":!regular") != -1):
 #if ircmsg.find(":!regular"):
 if get_user_level(ircmsg) == 100:
  twitch_account_id = ircmsg.split(":!regular ", 2)[1]
  set_regular(twitch_account_id)
 #else: Send_message("Sorry $user! You do not have sufficient rights."

#!rules - not yet implemented
if (ircmsg.find(":!rules") != -1):
 Send_message("(1) Please be respectful. (2) Healthy debate is encouraged.  Be prepared to cite your sources.")

#!twitter
if (ircmsg.find(":!twitter") != -1):
 Send_message("Twitter: http://forcethestorm.twitter.com/")

#!website
if (ircmsg.find(":!website") != -1):
 Send_message("Website: http://www.forcethestorm.com/")
 
#!youtube - not yet implemented
if (ircmsg.find(":!youtube") != -1):
 Send_message("Sorry, !help is not functional yet.  Check back soon!")


#if (ircmsg.find(":!commands") or ircmsg.find(":!help")):
 #Send_message("Commands available: !card card name")
#if ircmsg.find(":!regular"):
 #if ircmsg.find(":!regular"):
 #if Twitch_Users.Security_ID = 100
  #set_regular(ircmsg.split(":!regular ", 2)[1])
 #else: Send_message("Sorry $user! You do not have sufficient rights."

#var -g %punt = 0
#%punt 4
#var -g %puns = 0
#%puns 4
#var -g %craig = 0
#%craig = 1
#var -g %decklist
#%decklist = unknown
