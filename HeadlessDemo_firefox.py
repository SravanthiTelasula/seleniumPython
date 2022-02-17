from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()

options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://google.com/")
print(driver.title)
print ("Headless Firefox Initialized")
driver.quit()