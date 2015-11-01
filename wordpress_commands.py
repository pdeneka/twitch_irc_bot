import credentials
import xmlrpclib
import sys

host = credentials.WORDPRESS_HOST
username = credentials.WORDPRESS_USERNAME
password = credentials.WORDPRESS_PASSWORD

def Get_Last_Article():
 server = xmlrpclib.ServerProxy(credentials.WORDPRESS_XMLRPC)
 result = server.metaWeblog.getRecentPosts(host, username, password, 1, 1, 1)
 link = str(result[0]).split("'permaLink': '")[1].split("', '")[0]
 title = str(result[0]).split("'title': '")[1].split("', '")[0]
 article_info = "\"" + title + "\": " + link
 return article_info
