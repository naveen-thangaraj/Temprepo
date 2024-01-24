# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:21:33 2024

@author: naveen
"""

# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    print('Testing Script has been started')
    conn = mariadb.connect(
        host='10.107.48.42',
        port=3306,
        username='root',
        password='Sunshine@321#',
        database='cholams'
    )
    if conn:
        print('Connection sucessfull')
    else:
        sys.exit()
        
    cur = conn.cursor()
        
        
    # Getting data from claim_data table
    cur.execute("""select  count(*) from cholams.claim""")
    claim_data = cur.fetchall()
    print(claim_data)
    
    ###############################################################################
    
    # Getting data from claim_output table
    cur.execute("""select count(*) from  cholams.claim_output""")
    claim_output = cur.fetchall()
    print(claim_output)
    
    ##############################################################################
    
    # Getting data from model_meter table
    cur.execute("""select count(*) from cholams.model_meter""")
    model_meter = cur.fetchall()
    print(model_meter)
    
    # Make the changes to the database persistent
    # conn.commit()
    
    # Close cursor and communication with the database
    
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    
cur.close()
conn.close()
