import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("http://124.30.111.67/covid19/SDFForm.asp")
print(driver.title)
text=driver.find_element_by_name("ccno")
text.send_keys("46430")
text.send_keys(Keys.RETURN)
tablabtext=driver.find_element_by_id("preyes_id")
tablabtext.click()
tablabtext=driver.find_element_by_id("oxymeterno")
tablabtext.click()
tablabtext=driver.find_element_by_id("feverno_id")
tablabtext.click()
tablabtext=driver.find_element_by_id("covidtestno_id")
tablabtext.click()
tablabtext=driver.find_element_by_id("quarantineno_id")
tablabtext.click()
tablabtext=driver.find_element_by_id("highriskno")
tablabtext.click()
tablabtext=driver.find_element_by_id("travelno")
tablabtext.click()
tablabtext=driver.find_element_by_id("senseno")
tablabtext.click()
tablabtext=driver.find_element_by_id("travel50KMSno")
tablabtext.click()
tablabtext=driver.find_element_by_id("famtravelno")
tablabtext.click()
tablabtext=driver.find_element_by_id("famriskareano")
tablabtext.click()
tablabtext=driver.find_element_by_name("insert")
tablabtext.click()
time.sleep(15)
driver.quit()
