from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'turkish')
from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd
import pymysql.cursors
import pyautogui



connection = pymysql.connect(host='****', user='root',password='*',database='sakila',cursorclass=pymysql.cursors.DictCursor)
mycursor = connection.cursor()

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://twitter.com/login?lang=tr"
driver.get(url)
time.sleep(2)

kullaniciad1 = ""
password1 = ""

kullaniciad = driver.find_element_by_name("session[username_or_email]")
kullaniciad.send_keys(kullaniciad1)
time.sleep(1)

sifre = driver.find_element_by_name("session[password]")
sifre.send_keys(password1)
time.sleep(1)

giris = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div > div")
giris.click()
time.sleep(1)

Dahafazla = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/div/div/div[2]/span")
Dahafazla.click()
time.sleep(1)

Ayarlar = driver.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[9]/a/div")
Ayarlar.click()
time.sleep(1)

Gizlilik = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/section[1]/div[2]/div/div[3]/a/div/div/div")
Gizlilik.click()
time.sleep(1)

Engel = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[4]")
Engel.click()
time.sleep(1)

Block = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[1]")
Block.click()
time.sleep(1)

ekran_goruntusu = pyautogui.screenshot()
dosya_adi = "anlık.jpg"
ekran_goruntusu.save(dosya_adi)


scroll = 0
sayac = 0 
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height 
    Blocklist = driver.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
    for i in Blocklist:   
        takip =  ("https://twitter.com/" + i.text)
        print(takip)
        sql = "INSERT INTO  blocked (engelli) VALUES (%s)"
        val = (takip)
        mycursor.execute(sql, val)
        
        
connection.commit()
driver.quit()
print("Başarıyla Tamamlandı.")








