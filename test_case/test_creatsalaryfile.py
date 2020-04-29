# -*- coding: utf-8 -*-
#from seleniumlearning.test_case.enymlogin import Login

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import win32gui
import win32con
import unittest
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append("D:\\gitworkspace")
sys.path.append("D:\\gitworkspace\\testAuto")
sys.path.append("D:\\gitworkspace\\testAuto\\test_case")
from testAuto.test_case.enymlogin import Login

login_new = Login()
login_new.login()
login_new.driver.maximize_window()


class CreatsalaryfileTest(unittest.TestCase):
    def test_creatsalaryfile(self):

        # 点击我要发薪
        login_new.driver.find_element_by_css_selector('.content-salary').click()
        time.sleep(1)
        element = login_new.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        # 点击创建发放单
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-steps-item:nth-child(4) .ant-steps-item-title").click()
        #login_new.driver.find_element_by_xpath("//*[@id=\"root\"]/span/section/main/div/div/section/div/div[2]/header/div/div/div[4]/div/div[3]/div[1]").click()
        time.sleep(1)

        # 点击添加数据
        login_new.driver.find_element_by_xpath("//*[@id=\"root\"]/span/section/main/div/div/section/section/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div/span/button").click()
        # actions = ActionChains(login_new.driver)
        # actions.move_to_element(element).perform()
        element = login_new.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()
        # js = 'document.getElementsByClassName("ant-calendar-picker-input ant-input")[0].removeAttribute("readonly")'
        # login_new.driver.execute_script(js)
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-col-14 .ant-calendar-picker-input").click()
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()
        # login_new.driver.find_element(By.CSS_SELECTOR, ".ant-calendar-picker-input.ant-input").send_keys("五月")
        login_new.driver.find_element(By.LINK_TEXT, "五月").click()
        # 上传文件
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-row:nth-child(2) .ant-btn").click()
        time.sleep(1)
        # win32gui
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'D:\pycc\seleniumforpython\1036对私-虚户2.xls')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        time.sleep(2)

        # 选择摘要
        login_new.driver.find_element(By.CSS_SELECTOR, "#roundup .ant-select-selection__placeholder").click()
        time.sleep(1)
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-select-dropdown-menu-item-active").click()
        time.sleep(1)
        # 点击提交
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(2)").click()
        time.sleep(1)

        # 提交数据页面刷新按钮
        login_new.driver.find_element_by_xpath("//*[@id=\"root\"]/span/section/main/div/div/section/section/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div[1]/button").click()
        time.sleep(2)
        #点击提交数据页面提交按钮
        login_new.driver.find_element(By.XPATH,"//*[@id=\"root\"]/span/section/main/div/div/section/section/div/div/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/span[1]/div/div/span").click()
        time.sleep(1)
        #弹框确定按钮
        login_new.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/div/div[2]/div/div[2]/button[2]").click()
        time.sleep(2)
        #点击发送审核按钮
        login_new.driver.find_element_by_xpath("/html/body/div[1]/span/section/main/div/div/section/section/div/div/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[9]/div/span[1]/div/div/span").click()
        time.sleep(1)
        #点击发送审核弹窗的确定按钮
        login_new.driver.find_element_by_css_selector(".popover-confirm-btn > button:nth-child(2)").click()
        time.sleep(2)

        element = login_new.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        #login_new.driver.quit()


        # 点击薪资审核发放菜单签页
        login_new.driver.find_element_by_xpath("//*[@id=\"root\"]/span/section/main/div/div/section/div/div[2]/header/div/div/div[5]/div").click()
        time.sleep(1)


        # 薪资发放点击审核通过
        login_new.driver.find_element(By.CSS_SELECTOR, "#root > span > section > main > div > div > section > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > div > div:nth-child(1) > button.ant-btn.ant-btn-primary.ant-btn-sm").click()
        time.sleep(1)
        # 确认审核批次
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-modal-confirm-btns > .ant-btn-danger").click()
        time.sleep(2)

        element = login_new.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()

        # 薪资发放,点击发放弹出输入发薪密码
        login_new.driver.find_element(By.CSS_SELECTOR, "#root > span > section > main > div > div > section > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div.ant-table-wrapper > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(11) > div > div > div:nth-child(1) > button.ant-btn.ant-btn-primary.ant-btn-sm").click()
        time.sleep(2)
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()
        login_new.driver.find_element(By.ID, "salarypayform_in_modal_pass_word").click()

        login_new.driver.find_element(By.ID, "salarypayform_in_modal_pass_word").send_keys("123qweAS")

        # 输入密码点击确定
        login_new.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(2)").click()
        time.sleep(5)
        #login_new.driver.refresh()
        element = login_new.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(login_new.driver)
        actions.move_to_element(element).perform()
        login_new.driver.find_element_by_xpath("//*[@id=\"root\"]/span/section/main/div/div/section/section/div/div/div/div/div[3]/div[1]/div[2]/div[1]/form/div[5]/div/div/span/button[1]").click()
        time.sleep(2)
        login_new.driver.find_element_by_xpath("//*[@id=\"root\"]/span/section/main/div/div/section/div/div[2]/header/div/div/div[5]/div").click()
        login_new.driver.switch_to.window(login_new.driver.window_handles[0])
        time.sleep(1)
        # 获取发放的状态
        table = login_new.driver.find_element(By.CSS_SELECTOR, ".ant-table-tbody")
        time.sleep(2)

        rows_1 = table.find_elements_by_tag_name('tr')[0]
        # print(rows_1)
        td = rows_1.find_elements_by_tag_name('td')
        # print(td[8])
        celldata_8 = td[8].text
        # print(celldata_8)

        if celldata_8 == '已发放':
            rep = "通过"
            print(rep)

        else:
            rep = "未通过"
            print(rep)

        login_new.driver.quit()


if __name__ == "__main__":
    unittest.main()

