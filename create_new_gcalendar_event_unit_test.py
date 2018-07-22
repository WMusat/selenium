'''
This script will log into a google account, navigate to the calendar, and create a new event
You will need to add your account details into the variables below

The name of the event will be unique each time to help avoid false positives from failed test runs
There is 3 error checks along the way:
1. make sure you logged into your account okay
2. make sure you navigated to the new event page
3. make sure the event got created 


'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#dont change login url
loginURL="https://calendar.google.com"
#add your username
loginName="user.person@gmail.com"
#add your pw
loginPW="PASSWORD123"
#do not alter the newEventURL
newEventURL="https://calendar.google.com/calendar/r/eventedit?pli=1"
#add your user name here with a space - this is needed for error checking
#For example, if you account is rick.james@gmail,com - enter Rick James below
userName="User Person"




class StanzaTest(unittest.TestCase):
    @classmethod
    def setUp(inst):
        #if your webdriver is located in a different folder you may need to change the path below
        inst.driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
        inst.driver.implicitly_wait(5)
        inst.driver.maximize_window()
        inst.driver.get(loginURL)
        inst.driver.title
        inst.mouse = webdriver.ActionChains(inst.driver)
        inst.time = time

    def test_1_create_event(self):
        #start login
        self.uname = self.driver.find_element_by_id("identifierId")
        self.uname.send_keys(loginName)
        self.driver.find_element_by_id("identifierNext").click()
        time.sleep(3)
        self.passwd = self.driver.find_element_by_name("password")
        self.passwd.send_keys(loginPW)
        self.driver.find_element_by_id("passwordNext").click()
        #make sure you logged in okay by checking user name is visible
        loginCheck = self.driver.find_element_by_tag_name('body').text
        self.assertTrue( userName in loginCheck)
        #move to new event page and make sure you made it to event page
        self.driver.get(newEventURL) 
        eventCheck = self.driver.find_element_by_tag_name('body').text
        self.assertTrue("Add title" in eventCheck)
        time.sleep(2)  
        #get timestamp and create event named after the timestamp
        #the reason for this is if the 'delete an event' unit test breaks this one still works
        self.ts = time.strftime("%c")
        self.EventTitle = self.driver.find_element_by_id("xTiIn")
        self.EventTitle.send_keys(self.ts)
        time.sleep(2)
        #save event
        self.Save = self.driver.find_element_by_id("xSaveBu").click()
        #make sure event got created by checking the unique time stamp taken earlier
        createdCheck = self.driver.find_element_by_tag_name('body').text
        self.assertTrue(self.ts in createdCheck)

    @classmethod
    def tearDown(inst):
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()



