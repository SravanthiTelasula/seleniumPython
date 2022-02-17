from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate
import time
from datetime import datetime

sleep_tran = 0.5

Data_list =[]
Data_list.append(['City/Cousine', 'County/State Name', 'New Cases', 'New Deaths'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()

#Search for "covid collin county numbers"
time.sleep(sleep_tran)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("covid collin county numbers")
time.sleep(sleep_tran)
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
time.sleep(sleep_tran)

try:
    NewCases = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/span').text
except:
    NewCases = 0
    print("No newcase field found")

try:
    NewDeaths = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div[2]/div/span').text
except:
    NewDeaths = 0
    print("No NewDeaths field found")

Data_list.append(['Frisco(Home)', 'Collin', NewCases, NewDeaths])

print(Data_list)


#Search for "covid Fairfax county numbers"
time.sleep(sleep_tran)
driver.get("https://www.google.com")
time.sleep(sleep_tran)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('covid Fairfax county numbers')
time.sleep(sleep_tran)
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
time.sleep(sleep_tran)

try:
    NewCases = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/span').text
except:
    NewCases = 0
    print("No newcase field found")

try:
    NewDeaths = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div[2]/div/span').text
except:
    NewDeaths = 0
    print("No NewDeaths field found")

Data_list.append(['Arlington', 'Fairfax', NewCases, NewDeaths])
print(Data_list)

#Search for "covid San joaquin county numbers"
time.sleep(sleep_tran)
driver.get("https://www.google.com")
time.sleep(sleep_tran)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('covid San joaquin county numbers')
time.sleep(sleep_tran)
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
time.sleep(sleep_tran)

try:
    NewCases = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/span').text
except:
    NewCases = 0
    print("No newcase field found")

try:
    NewDeaths = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div[2]/div/span').text
except:
    NewDeaths = 0
    print("No NewDeaths field found")

Data_list.append(['Tracy(Ved home)', 'San Joaquin/SFO', NewCases, NewDeaths])
print(Data_list)


#Search for "covid Norfolk County county numbers"
time.sleep(sleep_tran)
driver.get("https://www.google.com")
time.sleep(sleep_tran)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('covid Norfolk County county numbers')
time.sleep(sleep_tran)
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
time.sleep(sleep_tran)

try:
    NewCases = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/span').text
except:
    NewCases = 0
    print("No newcase field found")

try:
    NewDeaths = driver.find_element(By.XPATH,'//*[@id="eTST2"]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div[2]/div/span').text
except:
    NewDeaths = 0
    print("No NewDeaths field found")

Data_list.append(['Boston(Snigdha home)', 'Norfolk County', NewCases, NewDeaths])
print(Data_list)

print(tabulate(Data_list, tablefmt='html'))

now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M%S")


HTML_Filename = 'My_Covid_Dashboard_' + date_time + '.html'

print('Entering the html file wirting')
f = open(HTML_Filename, "a")
f.write(tabulate(Data_list, tablefmt='html'))
html_content = tabulate(Data_list, tablefmt='html')
f.close()

driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))