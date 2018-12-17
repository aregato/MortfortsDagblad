import MySQLdb

# Upprättar en anslutning till databasen
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="", db="loggilue")

# Olika cursors för att utföra olika saker

# Login, signup
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# Dropdown
cursor2 = db.cursor()
