# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:24:51 2023
@author: Naveen Thangaraj
"""

# Package import

import pandas as pd
import boto3
import mysql.connector


# Set the connection details
connection_config = {
    'user': 'root',
    'password': 'Sunshine@321#',
    'host': '10.107.48.42',
    'database': 'cholams',
    'port': '3306'
}

# Establish a connection to the database
connection = mysql.connector.connect(**connection_config)

try:
    # Check the connection status
    #if connection_string:
    if connection.is_connected():
        print("Connection successfully established")
    else:
        print('Connection to the host failed')
except Exception as e:
    print(e)
