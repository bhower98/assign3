import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Cart_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://team2store.pythonanywhere.com/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[3]").click()
       time.sleep(1)