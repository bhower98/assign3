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
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
       author = "student"
       elem = driver.find_element_by_id("id_author")
       elem.send_keys(author)
       title = "test"
       text = "test text"
       elem = driver.find_element_by_id("id_title")
       elem.send_keys(title)
       elem = driver.find_element_by_id("id_text")
       elem.send_keys(text)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/p/span[1]/a[1]").click()
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/p/span[2]/a[1]").click()
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[1]/a[1]").click()
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[2]/a[1]").click()
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(1)
       action = "delete"
       elem = driver.find_element_by_name("action")
       elem.send_keys(action)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[2]/td/input").click()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").click()

       time.sleep(1)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()