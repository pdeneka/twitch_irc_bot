import credentials
import xmlrpclib
import sys

host = credentials.WORDPRESS_HOST
username = credentials.WORDPRESS_USERNAME
password = credentials.WORDPRESS_PASSWORD
xmlrpc = credentials.WORDPRESS_XMLRPC

def Get_Last_Article():
 try:
  server = xmlrpclib.ServerProxy(xmlrpc)
  result = server.metaWeblog.getRecentPosts(1, username, password, 1, 1)
  link = str(result[0]).split("'permaLink': '")[1].split("', '")[0]
  title = str(result[0]).split("'title': '")[1].split("', '")[0]
  article_info = "\"" + title + "\": " + link
  return article_info
 except:
  return "-1"



def Get_Article_with_Tags():
 print "wordpress_commands.Get_Article_with_Tags() is not yet implemented."
