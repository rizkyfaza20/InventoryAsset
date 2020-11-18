#!/bin/usr/python

import requests
import subprocess
import os
import datetime

nama_file = 'report_file.xlsx'
timestamp = datetime.datetime.now()
t = timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second

def connect_server(credentials):
    """
    Credentials to login in Lansweeper Area
    """
    url = 'http://192.168.6.127:81/login.aspx'
    credentials = { 'username' : 'it73', 
                'password' : 'pindadit73!'}
    # In this session you've been logged in to Web Server
    r = requests.post(url, data=credentials)

    url_report = 'http://192.168.6.127:81/export.aspx?export=xls&det=Web50getdevicebytype&title=All+Windows+assets&@devicetype=-1'
    r = requests.get(url_report)

    """
    Line above used for crawl and download data from the specific URL
    """
    with open('Web50getdevicebytype.xlsx','wb') as f:
        f.write(r.content)
        os.rename('Web50getdevicebytype.xlsx',nama_file + '_' + '-'.join(t))
