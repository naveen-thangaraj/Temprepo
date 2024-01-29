# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:47:36 2024

@author: naveen
"""

import cx_Oracle
 
con = cx_Oracle.connect('ins/ins620@10.105.24.10:1521/ggpoc')

if con:
   print('Connection Establish') 
else:
   print('Connection not working')
 
  
