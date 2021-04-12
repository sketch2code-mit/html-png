# this is the coding for generating html screenshot
# written by Doodle2Code team for MIT 6.962 Applied Machine Learning

import time
from selenium import webdriver
import os

c = 0
n = 0
j = 0
i = 0

for c in range(3):
    for n in range(10):
        for j in range(10):
            for i in range(10):
                # name of the file in format of 0000.html
                fn = str(c)+str(n)+str(j)+str(i)+".html"
                path = '/Users/Username/Desktop/filename/'
                tmpurl = 'file://{path}/{mapfile}'.format(
                    path=path, mapfile=fn)  # find the address of the html
                driver = webdriver.Chrome()
                driver.maximize_window()
                # maximum waiting time for opening the html
                driver.implicitly_wait(6)
                driver.get(tmpurl)  # open html
                time.sleep(1)
                # print("done')

            driver.get_screenshot_as_file(
                str(c)+str(n)+src(j)+str(i)+".png")  # rename the file
