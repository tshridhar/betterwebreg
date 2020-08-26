""" FUTURE VERSION WILL BE HEADLESS """
""" THIS IS A TESTING BUILD         """

from pathlib import Path
class Executor:
    def __init__(self, file : "Open file", driver : "WebDriver"):
        self._info = {"username" : "", "password" : "", "instructions" : []}
        self._file = file
        self.driver = driver
        self._read_from_file()

    def _read_from_file(self):
        self._info["username"], self._info["password"] = self._file.readline().rstrip().split()
        for i in self._file.readlines():
            self._info["instructions"].append(tuple(i.rstrip().split()))

    def _login(self):
        self.driver.find_element_by_id("ucinetid").send_keys(self._info["username"])
        self.driver.find_element_by_id("password").send_keys(self._info["password"])
        self.driver.find_element_by_xpath("//input[@type ='submit']").click()

    def _logout(self):
        self.driver.find_element_by_xpath("//input[@value='Logout']").click()
        self.driver.quit()

    def _exec(self):
        for i in self._info["instructions"]:
            driver.find_element_by_id("{instr}".format(instr=i[0].lower())).click()
            driver.find_element_by_xpath("//input[@name='courseCode']").send_keys(i[1])
            driver.find_element_by_xpath("//input[@value='Send Request']").click()

    def run(self):
        self._login()
        self.driver.find_element_by_xpath("//input[@value='Enrollment Menu']").click()
        self._exec()
        self._logout()

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
c.run()

f.close()