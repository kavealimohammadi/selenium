# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestMainMenu():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://10.131.1.111:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mainMenu(self):
    self.driver.get("https://test1401.sormas-oegd.de//sormas-ui/login")
    self.driver.set_window_size(1920, 1200)
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").send_keys("sadmin38124")
    self.driver.find_element(By.ID, "Login.doLogIn").click()
    self.driver.get("https://test1401.sormas-oegd.de//sormas-ui/")
    self.driver.set_window_size(1920, 1200)
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-lg-6 > .v-horizontallayout > .v-expand > .v-slot:nth-child(1)")))
    self.driver.find_element(By.CSS_SELECTOR, "#tasks .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".vspace-3 .v-align-right")))
    self.driver.find_element(By.CSS_SELECTOR, "#cases .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".vspace-3 .v-align-right")))
    self.driver.find_element(By.CSS_SELECTOR, "#aggregatereports .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-grid-tablewrapper")))
    self.driver.find_element(By.CSS_SELECTOR, "#contacts .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".vspace-3 .v-align-right")))
    self.driver.find_element(By.CSS_SELECTOR, "#events .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-slot:nth-child(13)")))
    self.driver.find_element(By.CSS_SELECTOR, "#samples .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".vspace-3 .v-align-right")))
    self.driver.find_element(By.CSS_SELECTOR, "#reports .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-margin-top .v-slot:nth-child(2)")))
    self.driver.find_element(By.CSS_SELECTOR, "#statistics .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-expand > .v-slot > .v-margin-top")))
    self.driver.find_element(By.CSS_SELECTOR, "#users .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-slot-vspace-3")))
    self.driver.find_element(By.CSS_SELECTOR, "#configuration .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-grid-tablewrapper")))
    self.driver.find_element(By.CSS_SELECTOR, "#about .valo-menu-item-caption").click()
    WebDriverWait(self.driver, 10000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".v-slot-about-content")))
    self.driver.find_element(By.ID, "actionSettings").click()
    self.driver.find_element(By.CSS_SELECTOR, ".v-menubar-menuitem-selected > .v-menubar-menuitem-caption").click()
    self.driver.find_element(By.ID, "commit").click()
    self.driver.find_element(By.CSS_SELECTOR, "#actionSettings .v-menubar-menuitem-caption").click()
    self.driver.find_element(By.ID, "gwt-uid-4").click()
    self.driver.find_element(By.ID, "discard").click()
    self.driver.find_element(By.CSS_SELECTOR, "#actionSettings .v-menubar-menuitem-caption").click()
    self.driver.find_element(By.CSS_SELECTOR, ".v-filterselect-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".gwt-MenuItem-selected").click()
    self.driver.find_element(By.ID, "commit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".v-horizontallayout > .v-expand").click()
    self.driver.find_element(By.CSS_SELECTOR, "#actionLogout .v-menubar-menuitem-caption").click()
    self.driver.find_element(By.ID, "username").send_keys("admin")
    self.driver.find_element(By.ID, "password").send_keys("sadmin38124")
  
