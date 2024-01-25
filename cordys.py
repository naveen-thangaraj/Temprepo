import oracledb

connection = oracledb.connect(user="ins", password="ins610",
                              dsn=" 10.105.24.18:1521/orclpdb")

if connection:
    print('connection sucessfull')
else:
    print('connection not working')
