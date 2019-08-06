import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       assert "Logged In"
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a").click()
       user = "tester"
       passw = "testman1a"
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys(passw)
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys(passw)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/a[3]").click()
       time.sleep(1)
       action = "delete"
       elem = driver.find_element_by_name("action")
       elem.send_keys(action)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[3]/td[1]/input").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").click()
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()