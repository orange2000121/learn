# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:12:40 2021

@author: danny
"""

import qrcode
codetext='http://cdn.thu.edu.tw/index.php'
img=qrcode.make(codetext)
img.save('thu.jpg')