# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pymysql
from selenium.common.exceptions import NoSuchElementException
import HTMLTestRunner
import unittest
import win32gui
import win32con



class Login():
    def login(self):
        #option = webdriver.ChromeOptions()
        #option.binary_location = r'C:\Users\Jenny\AppData\Local\Google\Chrome\Application\chrome.exe'
        self.driver = webdriver.Chrome(r'C:\Users\Jenny\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        #self.driver = webdriver.Chrome()
        self.driver.get("https://192.168.10.20/enym/login")

        #self.driver.set_window_size(1081, 574)
        self.driver.maximize_window()
        #self.driver.find_element(By.ID, "businessCode").click()
        #self.driver.find_element(By.ID, "businessCode").send_keys("1036")
        self.driver.find_element(By.ID, "mobile").click()
        self.driver.find_element(By.ID, "mobile").send_keys("15563886995")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123qweAS")
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".login-form-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        self.driver.find_element(By.ID, "mobileCode").click()
        time.sleep(1)

        db = pymysql.connect(
            host='192.168.10.20',
            user='root',
            password='Hf!@7899',
            port=3306,
            database='youmidb',
            charset='utf8')
        cursor = db.cursor()
        sql = "SELECT mobile_code FROM en_mobile_code WHERE mobile ='15563886995'  AND STATUS = '1' AND DATE_FORMAT(create_time,'%Y-%m-%d') LIKE DATE_FORMAT(NOW(),'%Y-%m-%d') ORDER BY create_date DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        # print(result[0])
        db.close()

        self.driver.find_element(By.ID, "mobileCode").send_keys(result[0])
        self.driver.find_element(By.CSS_SELECTOR, ".login-form-button").click()

        element = self.driver.find_element(By.CSS_SELECTOR, ".login-form-button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 登录后获取所在页面
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        try:
            find_text = self.driver.find_element_by_css_selector('.ant-col.ant-col-offset-2.ant-col-lg-4.ant-col-xxl-4')
        except NoSuchElementException as e:
            print('未登录到首页')

        else:
            print('登录成功')


if __name__ == '__main__':
    login = Login()
    login.login()