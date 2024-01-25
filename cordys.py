# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:14:38 2024

@author: naveen
"""

# importing module
import cx_Oracle


con = cx_Oracle.connect('ins/ins610@10.107.62.18:1521')

if con:
    print("Connection establish successfully")
else:
    print("Connection not working")

