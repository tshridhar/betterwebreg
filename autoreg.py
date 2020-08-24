SITE_URL = "https://www.reg.uci.edu/cgi-bin/webreg-redirect.sh"
f = open("info.txt", 'r')

USERNAME = f.readline().strip()
PASSWORD = f.readline().strip()
CLASSES = ["placeholder"]

# pip install chromedriver-py==84.0.4147.30
from selenium import webdriver
from chromedriver_py import binary_path

driver = webdriver.Chrome(executable_path=binary_path)
driver.get(SITE_URL)
html = driver.page_source
user_form = driver.find_element_by_id("ucinetid")
pass_form = driver.find_element_by_id("password")
submit_button = driver.find_element_by_xpath("//input[@type ='submit']")

user_form.send_keys(USERNAME)
pass_form.send_keys(PASSWORD)
submit_button.click()

enrollment_menu_button = driver.find_element_by_xpath("//input[@value='Enrollment Menu']")
enrollment_menu_button.click()

### "ADD" Functionality disabled temporarily ####

# add_class_radio = driver.find_element_by_id("add")
# add_class_radio.click()

# course_code_form = driver.find_element_by_xpath("//input[@name='courseCode']")
# course_code_form.send_keys(CLASSES[0])

# request_button = driver.find_element_by_xpath("//input[@value='Send Request']")
# request_button.click()

logout_button = driver.find_element_by_xpath("//input[@value='Logout']")
logout_button.click()

f.close()

"""
HTML FOR REFERENCE

<input class="WebRegButton" value="Enrollment Menu" type=   "submit" name="submit">
<input type="radio" name="mode" value="add" id="add">
<input type="text" name="courseCode" size="5" maxlength="5">
<input type="submit" name="button" value="Send Request">
<input class="WebRegButton  WebRegLogoutButton" value="Logout" type="submit" name="submit">
"""