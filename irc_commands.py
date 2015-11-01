import pyodbc
from time import gmtime, strftime

def Get_Dailymotion():
 return "http://www.dailymotion.com/Forcing_The_Storm"

def Get_Facebook():
 return "https://www.facebook.com/pages/Forcing-The-Storm/"

def Get_Music():
 f = open('C:\Unp\unp_now_playing.txt')
 return f.readline()

def Get_Rules():
 return "(1) Be respectful. (2) Healthy debate is encouraged.  Be prepared to cite your sources."

def Get_Twitter():
 return "@forcethestorm"

def Get_Website():
 return "http://www.forcethestorm.com/"

def Get_YouTube():
 return "https://www.youtube.com/channel/UCQvU9i5-UTV1atVOSY8XJhQ"

#COMMANDS
#Craig
#Whisper
#HELP

#DECK
def Get_Deck():
 return "!deck is not yet implemented."

def Set_Deck(deckname):
 return "!setdeck is not yet implemented."
 #SQL Stored Procedure: Import Decks
 #track version of same deck
 #SQL Exports new decks to dropbox, webhost
 #returns deckname & link

#PUNS
#if (ircmsg.find(":!puns") != -1):
 #Send_message("Sorry, !puns is not functional yet.  Check back soon!")
 #on 100:TEXT:!puns:: { inc %puns 1 | msg $chan Pun added!  Total puns to date: %puns }
 #on 100:TEXT:!remove_pun:: { dec %puns 1 | msg $chan Pun removed!  Total puns to date: %puns }
 #on 1:TEXT:!puns:: { msg $chan Puns: %puns }

#PUNT
#if (ircmsg.find(":!punt") != -1):
 #Send_message("Sorry, !punt is not functional yet.  Check back soon!")
 #on 100:TEXT:!punt: { inc %punt 1 | msg $chan Punt added!  Total punts to date: %punt }
 #on 1:TEXT:!punt:: { msg $chan Punts: %punt }

#QUOTES
#if (ircmsg.find(":!addquote") != -1):
 #Send_message("Sorry, !addquote is not functional yet.  Check back soon!")
 #add quote (submitter, quote)
  #initiate confirm vote
   #on 2 votes, set quote active
 #remove quote (set active = 0)

#var -g %punt = 0
#%punt 4
#var -g %puns = 0
#%puns 4
#var -g %craig = 0
#%craig = 1
#var -g %decklist
#%decklist = unknown
