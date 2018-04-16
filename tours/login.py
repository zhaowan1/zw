'''
Created on 2018年4月4日

@author: Administrator
'''
# coding=utf-8

from selenium import webdriver
import time
zw = webdriver.Firefox()
zw.get('http://cn.bing.com')
zw.find_element_by_id('sb_form_q').send_keys('selenium')

zw.find_element_by_id('sb_from_go').click()
time.sleep(4)
zw.close()
