from selenium import webdriver;
driver=webdriver.Chrome("C:\\Python27\\chromedriver.exe");
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()