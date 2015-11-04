import mssql_credentials as m
import pyodbc
import sys


def oracle(card):
 credentials = 'DRIVER={SQL Server};SERVER=' + m.server
 credentials = credentials + ';DATABASE=' + m.database
 credentials = credentials + ';UID=' + m.user_id
 credentials = credentials + ';PWD=' + m.password
 connection = pyodbc.connect(credentials)
 cursor = connection.cursor()

 cursor.execute("SELECT Oracle_Text FROM python_Oracle WHERE lower(Card_Name) = lower(ltrim(rtrim(?)))", card)
 rows = cursor.fetchall()

 connection.close()
 oracle_text = ""

 for row in rows:
  oracle_text = row[0]
 return oracle_text


#Todo:
#Automatically Track & Update Followers
#Add Quotes, Puns, Punts, Craig

#Help here:
#https://code.google.com/p/pyodbc/wiki/StoredProcedures
