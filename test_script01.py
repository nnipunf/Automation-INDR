from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class LaunchBrowser():
    def startup(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://visa.vfsglobal.com/\n'
                   'ind/en/ita/login?fbclid=IwAR3pqMz3y7n9GJFFjGa-HjqGjH5L_\n'
                   'yV-1OZte2jVVATYsF88185rUPh3BPk')
        driver.implicitly_wait(10)
        time.sleep(5)

site_launch = LaunchBrowser()
site_launch.startup()