""" FUTURE VERSION WILL BE HEADLESS """
""" THIS IS A TESTING BUILD         """

from pathlib import Path
class Executor:
    def __init__(self, file : "Open file", driver : "WebDriver"):
        self._info = {"username" : "", "password" : "", "instruction" : []}
        self._file = file
        self.driver = driver
        self._read_from_file()

    def _read_from_file(self):
        self._info["username"], self._info["password"] = self._file.readline().rstrip().split()
        for i in self._file.readlines():
            self._info["instruction"].append(tuple(i.rstrip().split()))

    def _login(self):
        user_form = self.driver.find_element_by_id("ucinetid")
        pass_form = self.driver.find_element_by_id("password")
        submit_button = self.driver.find_element_by_xpath("//input[@type ='submit']")
        user_form.send_keys(self._info["username"])
        pass_form.send_keys(self._info["password"])
        submit_button.click()

    def _logout(self):
        logout_button = self.driver.find_element_by_xpath("//input[@value='Logout']")
        logout_button.click()

    def exec(self):
        self._login()
        enrollment_menu_button = self.driver.find_element_by_xpath("//input[@value='Enrollment Menu']")
        enrollment_menu_button.click()
        self._logout()

    ### "ADD" Functionality disabled temporarily ####

    # add_class_radio = driver.find_element_by_id("add")
    # add_class_radio.click()

    # course_code_form = driver.find_element_by_xpath("//input[@name='courseCode']")
    # course_code_form.send_keys(CLASSES[0])

    # request_button = driver.find_element_by_xpath("//input[@value='Send Request']")
    # request_button.click()

from selenium import webdriver
from chromedriver_py import binary_path

# SETUP CONST VAR
SITE_URL = "https://www.reg.uci.edu/cgi-bin/webreg-redirect.sh"
FILENAME = "inp.txt"

"""
==============Expected Input Format================
"Instruction" and "value" (excluding the first line, 
which should always be username/password)
e.g.
peteranteater anteaterpass
add 60000
add 60003
drop 10290
drop 10292
(in the order of desired execution)
===================================================
"""

# INITIALIZE DRIVER
driver = webdriver.Chrome(executable_path=binary_path)
driver.get(SITE_URL)

# OPEN 
f = open(Path(FILENAME), 'r')

c = Executor(f, driver)
c.exec()

f.close()