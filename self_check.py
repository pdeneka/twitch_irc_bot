import re

Errors = 0

#PERFORM TESTS ON THE FOLLOWING

#Imports
try:
 import credentials
except:
 print "import credentials failed."
 Errors += 1

try: 
 import irc_commands
except:
 print "import irc_commands failed."
 Errors += 1

try:
 import logging
except:
 print "import logging failed."
 Errors += 1

try:
 import mssql_commands
except:
 print "import mssql_commands failed."
 Errors += 1

try:
 import os
except:
 print "import os failed."
 Errors += 1

try:
 import pyodbc
except:
 print "import pyodbc failed."
 Errors += 1
 
try:
 import string
except:
 print "import string failed."
 Errors += 1
 
try:
 import socket
except:
 print "import socket failed."
 Errors += 1
 
try:
 import subprocess
except:
 print "import subprocess failed."
 Errors += 1
 
try:
 import sys
except:
 print "import sys failed."
 Errors += 1
 
try:
 import twitch_commands
except:
 print "import twitch_commands failed."
 Errors += 1

try:
 import wordpress_commands
except:
 print "import wordpress_commands failed."
 Errors += 1
 
try:
 from time import gmtime
except:
 print "import gmtime from time failed."
 Errors += 1
 
try:
 from time import strftime
except:
 print "import strftime from time failed."
 Errors += 1

#!article
try:
 url = wordpress_commands.Get_Last_Article()
 title = url.split(": ")[0]
 url = url.split(": ")[1]
 url_remnants = url.replace('http://www.forcethestorm.com/index.php/', '')
 pattern_date = re.compile(r'\d{4}/\d{2}/\d{2}/')
 url_remnants = pattern_date.sub('', url_remnants)
 pattern_title = re.compile(r'[^A-Za-z0-9/]')
 title = pattern_title.sub('-', title[1:len(title)-1].lower())
 while(title.find('--') != -1):
  title = title.replace('--', '-')
 url_remnants = url_remnants.replace(title, '')
 url_remnants = url_remnants.replace('/', '')

 if(url_remnants != ""):
  print "url remaining characters: \"" + url_remnants + "\""
except:
 print "wordpress_commands.Get_Last_Article() failed."
 Errors += 1

#!card [name]
try:
 oracle_text = mssql_commands.Get_Oracle_Text('Tarmogoyf')
 if(oracle_text == 'Does not exist in the database at this time.'):
  print "Known card Tarmogoyf not found in database.  Check database."
  Errors += 1 
except:
 print "!card failed for unknown reason.  Debug."
 Errors += 1 
 
#!craig
#!deck [name]
#!decklists
#!music
#Terminal(message) - breaking lines on " " to be implemented
#!twitter
#!uf (update followers)
#!website
 

#DO NOT TEST
#!quit
#!restart

#UNAVAILABLE COMMANDS
#!puns
#!punts
#!session: begin, end, stats, uptime
#!us (update subscribers)

print "Errors: " + str(Errors)
#return Errors
