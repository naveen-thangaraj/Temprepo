# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:12:23 2024

@author: naveen
"""

# Package import

# Module Imports
import mariadb
import sys
import pandas as pd

try:
     connection = mariadb.connect(
         host='10.107.48.42',
         port=3306,
         username='root',
         password='Sunshine@321#',
         database='cholams'
     )
     
     # Check the connection status
     if connection:
        
        print("Connection successfully established")
        
        # Open a cursor to perform database operations
        cur = connection.cursor()
        
        # Getting data from claim_data table
        cur.execute("""select  cc.claim_number, cc.trigger_type, cc.claim_type 
                       from cholams.claim CC Join cholams.model_meter  MM on 
                       cc.claim_number=mm.claim_number 
                       where mm.created_date >= convert('2023-09-01 00:00:00.000', datetime));
                    """)
        claim_data = cur.fetchall()
        claim_data_col = [i[0] for i in cur.description]
        
        claim_data_df = pd.DataFrame(claim_data, columns=claim_data_col)
        claim_data_df.to_csv('claim_data.csv', index=False)
        
        ###############################################################################
        
        # Getting data from claim_output table
        cur.execute("""select 
               CO.claim_number, 
               CO.policy_no, 
               CO.final_claim_amount_before_capping, 
               CO.policy_type_values, 
               CO.mode_of_claim_values,
               CO.hospital_state_name, 
               CO.intermediary_mapping_values, 
               CO.final_risk_grade_vf  
               from  cholams.claim_output CO JOIN cholams.model_meter MM ON CO. claim_number=MM. claim_number 
               where MM.created_date >= convert('2023-09-01 00:00:00.000', datetime)
               """)
        claim_output = cur.fetchall()
        claim_output_col = [i[0] for i in cur.description]
        
        claim_output_df = pd.DataFrame(claim_output, columns=claim_output_col)
        claim_output_df.to_csv('claim_output.csv', index=False)
        
        ##############################################################################
        
        # Getting data from model_meter table
        cur.execute("""select claim_number, api_return_code , created_date from cholams.model_meter 
                       where created_date >= convert('2023-09-01 00:00:00.000', datetime) """)
        
        model_meter = cur.fetchall()
        model_meter_col = [i[0] for i in cur.description]
        
        model_meter_df = pd.DataFrame(model_meter, columns=model_meter_col)
        
        model_meter_df.to_csv('model_meter.csv', index=False)
        
        # Make the changes to the database persistent
        # conn.commit()
        
        # Close cursor and communication with the database
        cur.close()
        connection.close()
     else:
        print('Connection host failed')
except Exception as e:
    print(e)
