import cx_Oracle
 
# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="ins", password="ins620",
                               dsn="10.105.24.10:1521/ggpoc")
if connection:
   print('Connection Establish') 
else:
   print('Connection not working')
 
  
