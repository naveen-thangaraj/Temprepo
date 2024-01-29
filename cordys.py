import oracledb

# connection = oracledb.connect(user="ins", password="ins610",
#                               dsn="10.105.24.18:1521/orclpdb")

# Increase the timeout to 60 seconds
connection = oracledb.connect(user='ins', password='ins620', dsn='10.105.24.18:1521/ggpoc', timeout=60)

if connection:
    print('connection sucessfull')
else:
    print('connection not working')
