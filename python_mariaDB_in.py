#!/usr/bin/python
import MySQLdb

mariadb_connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="123456",  # your password
                     db="serv_info")        # name of the data base

cursor = mariadb_connection.cursor()

#retrieving information
var_serv_hostname = 'Server'
cursor.execute("SELECT serv_hostname_id,serv_hostname FROM serv_hostname_tab WHERE serv_hostname=%s", (var_serv_hostname,))
'''
for first_name, last_name in cursor:
    print("First name: {}, Last name: {}").format(serv_hostname_id,serv_hostname)
'''
#insert information
try:
    cursor.execute("INSERT INTO serv_hostname_tab (serv_hostname) VALUES (%s)", ('Maria DB'))
except mariadb.Error as error:
    print("Error: {}".format(error))

mariadb_connection.commit()
print "The last inserted id was: ", cursor.lastrowid

mariadb_connection.close()
