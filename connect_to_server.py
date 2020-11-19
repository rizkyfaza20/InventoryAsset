#!/bin/usr/python3

import requests
import os
import datetime

def connect_server(credentials):
    """
    Credentials to login in Lansweeper Area
    """
    url = 'http://192.168.6.127:81/login.aspx'
    credentials = { 'username' : 'it73', 
                'password' : 'pindadit73!'}
    # In this session you've been logged in to Web Server
    r = requests.post(url, data=credentials)
    return(credentials)


