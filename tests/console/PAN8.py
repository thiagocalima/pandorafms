# -*- coding: utf-8 -*-
from include.common_classes_60 import PandoraWebDriverTestCase
from include.common_functions_60 import login, click_menu_element, detect_and_pass_all_wizards, logout
from include.agent_functions import create_agent, search_agent
from include.user_functions import create_user
from include.module_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PAN8(PandoraWebDriverTestCase):

	test_name = u'PAN_8'
	test_description = u'Create agent and two modules, one without tag and with tag, create a user with tag and check this user can view module with tag and user can´t view module without tag'
	tickets_associated = []

	def test_pan8(self):

		driver = self.driver
		login(driver)
		detect_and_pass_all_wizards(driver)
		
		create_agent(driver,"PAN_8",group="Applications",ip="192.168.50.50")
		
		#We create a module without a tag
			
		create_module("network_server",driver,agent_name="PAN_8",module_name="Without tag",component_group="Network Management",network_component="Host Alive",ip="192.168.50.50")
		
		#We now create a modulo with tag "critical"
		
		create_module("network_server",driver,agent_name="PAN_8",module_name="With tag",component_group="Network Management",network_component="Host Alive",ip="192.168.50.50",tag_name="critical")

		
		l = [("Operator (Read)","All",["critical"])]

		create_user(driver,"PAN8_user","pandora",profile_list=l) 
		
		logout(driver,self.base_url)
		
		login(driver,user="PAN8_user")
		
		detect_and_pass_all_wizards(driver)
		
		search_agent(driver,"PAN_8")

		time.sleep(6)

		try:
			#The user should be able to see the module with Tag
			module = driver.find_element_by_xpath('//td[contains(.,"With tag")]')
			self.assertEqual("With tag" in driver.page_source,True)		
			
		except AssertionError as e:		
			self.verificationErrors.append(str(e))
		
		try:
			#The user should NOT be able to see the module without tag
			self.assertEqual("Without tag" in driver.page_source,False)
		except AssertionError as e:
			self.verificationErrors.append(str(e))
		

if __name__ == "__main__":
	unittest.main()
