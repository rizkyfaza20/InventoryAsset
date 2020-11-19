#!/bin/usr/python3

import requests
import os
import datetime
from connect-to-server import connect_server

nama_file = 'report_file.xlsx'
timestamp = datetime.datetime.now()
t = timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second


url_report = 'http://192.168.6.127:81/export.aspx?export=xls&det=Web50getdevicebytype&title=All+Windows+assets&@devicetype=-1'
r = requests.get(url_report)

#Line above used for crawl and download data from the specific URL

with open('Web50getdevicebytype.xlsx','wb') as f:
    f.write(r.content)
    os.rename('Web50getdevicebytype.xlsx',nama_file + '_' + '-'.join(t))
