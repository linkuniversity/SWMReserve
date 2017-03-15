#-*- coding: utf-8 -*-
from selenium import webdriver
import json

"""
!! Set reserve_config.json

USAGE --
python3 swm_reservation.py
"""

data = None

try:
    f = open('reserve_config.json')
    data = json.loads( f.read() )
    print(data)
except FileNotFoundError:
    print("Cannot find ./reserve_config.json!!")
    exit()

driver = webdriver.Chrome(data["chromedriver_src"])
driver.get('http://115.68.116.16/swmaestro/reservation.html')

name = driver.find_element_by_name("name1")
name.send_keys(data["name"])

phone = driver.find_element_by_name("phone")
phone.send_keys(data["phone"])

smButton = driver.find_element_by_xpath("//button[@class='btn w-xs btn-success']")
smButton.click()

driver.find_element_by_xpath("//select[@name='room_no']/option[text()='"+data["room"]+"']").click()

datepicker = driver.find_element_by_id('datepicker')
datepicker.clear()
datepicker.send_keys(data["date"])

st_time_hour = driver.find_element_by_xpath("//select[@name='st_time_hour']/option[text()='"+data["start_time"]+"']")
st_time_hour.click()

ed_time_hour = driver.find_element_by_xpath("//select[@name='ed_time_hour']/option[text()='"+data["end_time"]+"']")
ed_time_hour.click()

contents = driver.find_element_by_xpath("//input[@placeholder='회의내용']")
contents.send_keys(data["contents"])

attend_num = driver.find_element_by_id("man")
attend_num.send_keys(data["attend_num"])

member_num = driver.find_element_by_xpath("//input[@placeholder='연수생 번호']")
member_num.send_keys(data["member_number"])

confirm_btn = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
confirm_btn.click()

reserved_picker = driver.find_element_by_id("datepicker")
reserved_picker.clear()
reserved_picker.send_keys(data["date"])

driver.find_element_by_xpath("//button[@class='btn w-xs btn-success']").click()
