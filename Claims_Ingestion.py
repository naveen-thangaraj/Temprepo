# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:31:16 2024

@author: naveen
"""

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Sunshine@321#",
        host="10.107.48.42",
        port=3306,
        database="cholams"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

if conn:
    print('Connection successfully establish')
else:
    print('Connection has been failed')

