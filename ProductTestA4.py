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

       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[1]/a").click()
       elem = driver.find_element_by_name("category")
       name = "art"
       elem.send_keys(name)
       name = "test piece"
       elem = driver.find_element_by_id("id_name")
       elem.send_keys(name)
       time.sleep(1)
       desc = "This is a test description"
       elem = driver.find_element_by_id("id_description")
       elem.send_keys(desc)
       price = "80000"
       elem = driver.find_element_by_id("id_price")
       elem.send_keys(price)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
       time.sleep(1)
       driver.get("http://team2store.pythonanywhere.com/shop")
       time.sleep(1)
       driver.get("http://team2store.pythonanywhere.com/admin/shop/product/")
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[4]/table/tbody/tr[8]/td[1]/input").click()
       action = "delete"
       elem = driver.find_element_by_name("action")
       elem.send_keys(action)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/button").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").click()
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()