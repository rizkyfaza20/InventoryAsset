#!/bin/usr/python

import requests
import subprocess
import os


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
    with open() as target: