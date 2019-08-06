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

       validtodate = "2020-07-28"
       discount = "20"
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
       time.sleep(1)
       code = "testrun40"
       elem = driver.find_element_by_id("id_code")
       elem.send_keys(code)
       validfromdate = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/p/span[1]/a[1]").click()
       validfromtime = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[2]/div/p/span[2]/a[1]").click()
       elem = driver.find_element_by_id("id_valid_to_0")
       elem.send_keys(validtodate)
       validtotime = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[3]/div/p/span[2]/a[1]").click()
       elem = driver.find_element_by_id("id_discount")
       elem.send_keys(discount)
       active = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/label").click()
       save = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       driver.get("http://team2store.pythonanywhere.com/admin/coupons/coupon/")
       time.sleep(1)
       elem = driver.find_element_by_name("action")
       action = "delete"
       elem.send_keys(action)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td[1]/input").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").click()
       time.sleep(1)



   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()