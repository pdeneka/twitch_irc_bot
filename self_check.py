import credentials
import re

DEBUG = credentials.DEBUG
Errors = 0
Error_Message = ""


#PERFORM TESTS ON THE FOLLOWING

#Imports
try:
 import config
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"config\" failed.\n"

try:
 import credentials
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"credentials\" failed.\n"

try: 
 import irc_commands
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"irc_commands\" failed.\n"

try:
 import logging
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"logging\" failed.\n"

try:
 import mssql_commands
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"mssql_commands\" failed.\n"

try:
 import os
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"os\" failed.\n"

try:
 import pyodbc
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"pyodbc\" failed.\n"
 
try:
 import string
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"string\" failed.\n"
 
try:
 import socket
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"socket\" failed.\n"
 
try:
 import subprocess
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"subprocess\" failed.\n"
 
try:
 import sys
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"sys\" failed.\n"
 
try:
 import twitch_commands
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"twitch_commands\" failed.\n"
 

try:
 import wordpress_commands
except:
 Errors += 1
 Error_Message = Error_Message + "Import \"wordpress_commands\" failed.\n"

try:
 import time

 try:
  from time import gmtime
 except:
  Errors += 1
  Error_Message = Error_Message + "Import \"gmtime\" from \"time\" failed.\n"

 try:
  from time import strftime
 except:
  Errors += 1
  Error_Message = Error_Message + "Import \"strftime\" from time failed.\n"

except:
 Errors += 1
 Error_Message = Error_Message + "Import \"time\" failed.\n"


#!article
try:
 pattern_date = re.compile(r'\d{4}/\d{2}/\d{2}/')
 pattern_title = re.compile(r'[^A-Za-z0-9/]')
 pattern_url_base = re.compile(r'http://www.forcethestorm.com/index.php/')

 try:
  result = wordpress_commands.Get_Last_Article()
 except:
  Error_Message = Error_Message + "wordpress_commands.Get_Last_Article() - sub a\n"

 article_title = result.split(": ")[0]
 article_url = result.split(": ")[1]

 #remove the expected website base url: http://www.forcethestorm.com/index.php/
 url_remnants = pattern_url_base.sub('', article_url)

 #remove the expected date format: YYYY/MM/DD/
 url_remnants = pattern_date.sub('', url_remnants)

 #strip preceding and following quote
 #and convert anything not A-Z, a-z, 0-9 to hyphen
 article_title = pattern_title.sub('-', article_title[1:len(article_title)-1].lower()) 
 
 #replace multiple hypens with single hyphen
 while(article_title.find('--') != -1): 
  article_title = article_title.replace('--', '-')
 url_remnants = url_remnants.replace(article_title, '')
 url_remnants = url_remnants.replace('/', '')

 if(url_remnants.strip() != ""):
  Error_Message = Error_Message + "url remaining characters: \"" + url_remnants + "\"\n"
except:
 Error_Message = Error_Message + "wordpress_commands.Get_Last_Article() failed.\n"
 Errors += 1

#!card [name]
try:
 oracle_text = mssql_commands.Get_Oracle_Text('Tarmogoyf')
 if(oracle_text == 'Does not exist in the database at this time.'):
  Error_Message = Error_Message + "Known card \"Tarmogoyf\" not found in database.  Check database.\n"
  Errors += 1 
except:
 Error_Message = Error_Message + "!card failed for unknown reason.  Debug.\n"
 Errors += 1
 

#!decklists & !deck [name]
try:
 deck_names_list = mssql_commands.Get_Decklists()
 deck_names_list = deck_names_list[22:len(deck_names_list)]
 if(deck_names_list == "-1"):
  Errors += 1
  Error_Message = Error_Message + "Deck Names List returned \"-1\" instead of an actual list of deck names.\n"

 try:
  for deck_name in deck_names_list.split(', '):
   deck_url = mssql_commands.Get_WordPress_Decklist(deck_name)
   if(deck_url == "-1"):
    Error_Message = Error_Message + "\""+ deck_name + "\" not found.\n"
    Errors += 1
 except:
  Error_Message = Error_Message + "!decklists, !deck - sub a\n"

  try:
   if(mssql_commands.Get_WordPress_Decklist('this deck does not exist') != "-1"):
    Error_Message = Error_Message + "Incorrect deckname returned decklist.\n"
    Errors += 1
  except:
   Error_Message = Error_Message + "!decklists, !deck - sub b\n"
   
except:
 Error_Message = Error_Message + "!decklists, !deck - main\n"

#!music
 #irc_commands.Get_Music()
#roll d# 
#Terminal(message) - breaking lines on " " to be implemented
#!twitter
#!uf (update followers)
#!website
 

#DO NOT TEST
#!quit
#!restart

#UNAVAILABLE COMMANDS
#!quote (add, remove, display)
#!craig
#!puns
#!punts
#!session: begin, end, stats, uptime
#!us (update subscribers)
#!uv (update chat viewers)

if(Errors != 0):
 print "Errors: " + str(Errors)
 for error_line in Error_Message.split("\n"):
  print error_line
 #return Errors, Error_Message
else:
 print "Self-test completed without errors."
 #return 0



