from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Marko Idzan')

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()