""" FUTURE VERSION WILL BE HEADLESS """
""" THIS IS STILL A TESTING BUILD   """

from pathlib import Path
class Instruction:
    def __init__(self, file, driver):
        self._info = {"username" : [], "password" : [], "add" : [], "drop" : []}
        self.curr_instr = ""
        self.file = file
        self.driver = driver
        self._read_from_file()

    def _read_from_file(self):
        for i in self.file.readlines():
            if self.curr_instr in self._info.keys() and i.strip() not in self._info.keys():
                self._info[self.curr_instr].append(i.strip())
            self.curr_instr = i.strip() if i.strip() in self._info.keys() else self.curr_instr

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

    def exec_instr(self):
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

# INITIALIZE DRIVER
driver = webdriver.Chrome(executable_path=binary_path)
driver.get(SITE_URL)

# OPEN 
f = open(Path(FILENAME), 'r')

c = Instruction(f, driver)
c.exec_instr()

f.close()