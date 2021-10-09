#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pathlib
from bs4 import BeautifulSoup

doc = BeautifulSoup ('\n\n<!DOCTYPE html>\n<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark">\n  <head>\n    <meta charset="utf-8">\n  <link rel="dns-prefetch" href="https://github.githubassets.com">\n  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">\n  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">\n  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">\n  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>\n  <link rel="preconnect" href="https://avatars.githubusercontent.com">\n\n\n\n  <link crossorigin="anonymous" media="all" integrity="sha512-y7qmntuinsKc9vzjz7YzWWh8GcPQmvwoF4ULzjX7GgRSvik3SnIR2GIylHwLEF/3nya8RYtrrif1YX5IliJ1wA==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-cbbaa69edba29ec29cf6fce3cfb63359.css" />\n    <link crossorigin="anonymous" media="all" integrity="sha512-5495K7TraDdD0rUjH7go28D4vVQZ5ieXuCpiS3jv75MnUggsnjiA3JsOO5nbFy/PpjvO5yYu7KNfr4weDVEkMQ', 'html.parser')
print(doc)
#changing chromedriver default options
options = Options()
# options.headless = True
options.add_argument('window-size=1920x1080') #Headless = True

# web = 'https://sports.tipico.de/en/live/soccer' # what to scrape
web = 'https://twitter.com/explore/tabs/trending'
# web = 'https://cs.utexas.edu/~omeed'

# obtain the current path for debugging purposes.
x = pathlib.Path().resolve()

# obtain the chrome drivers path.
path = '/usr/local/bin/chromedriver' 

# for debugging..
# print("THIS IS THE PATH AGAIN: " + str(path))

# execute chromedriver with edited options
driver = webdriver.Chrome(path, options=options)

# obtain the link and open the webpage.
driver.get(web)

# 30 trending tags

tags = []

# box = driver.find_element_by_xpath('//div') #updated

# content = driver.find_element_by_css_selector('div .css-1dbjc4n')
contentTwo = driver.find_element_by_class_name('css-1dbjc4n r-1loqt21 r-6koalj r-1ny4l3l r-ymttw5 r-1f1sjgu r-o7ynqc r-6416eg') #updated
print(type(contentTwo))