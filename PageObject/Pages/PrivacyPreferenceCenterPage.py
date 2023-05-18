import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.insulet.com/"

class PrivacyPreferenceCenterPage:
    def __init__(self,driver):
        self.driver = driver;
        
        #Element identifiers.
        self.title = "ot-pc-title" #id
        self.description = "ot-pc-desc" #id
        self.learnMoreLink = "privacy-notice-link" #class
        self.acceptAll = "accept-recommended-btn-handler" #id
        
        #Manage Consent Preferences
        self.manageTitle = "ot-category-title" #id
        
        self.necessaryCookiesGroup = "//div[contains(@class, 'ot-accordion-layout')][1]/button" #xpath
        self.necessaryCookiesLabel = "ot-header-id-C0001" #id
        self.necessaryCookiesDescription = "ot-desc-id-C0001" #id
        self.necessaryCookiesButton = "ot-always-active" #class
        
        self.performanceCookiesGroup = "//div[contains(@class, 'ot-accordion-layout')][2]/button" #xpath
        self.performanceCookiesLabel = "ot-header-id-C0002" #id
        self.performanceCookiesDescription = "ot-desc-id-C0002" #id
        self.performanceCookiesCheckbox = "//div[contains(@class, 'ot-tgl')][1]/input" #xpath (has issues, looking into them)

        self.functionalCookiesGroup = "//div[contains(@class, 'ot-accordion-layout')][3]/button" #xpath
        self.functionalCookiesLabel = "ot-header-id-C0003" #id
        self.functionalCookiesDescription = "ot-desc-id-C0003" #id
        self.functionalCookiesCheckbox = "ot-group-id-C0003" #id

        self.targettingCookiesGroup = "//div[contains(@class, 'ot-accordion-layout')][4]/button" #xpath
        self.targettingCookiesLabel = "ot-header-id-C0004" #id
        self.targettingCookiesDescription = "ot-desc-id-C0004" #id
        self.targettingCookiesCheckbox = "ot-group-id-C0004" #id
        
        #Bottom Buttons
        self.rejectAll = "ot-pc-refuse-all-handler" #class
        self.saveChoices = "save-preference-btn-handler" #class
        
        
    def getTitle(self):
        return self.driver.find_element(By.ID,self.title).text
    
    def getDescription(self):
        return self.driver.find_element(By.ID,self.description).text
    
    def getLearnMoreText(self):
        return self.driver.find_element(By.CLASS_NAME,self.learnMoreLink).text
       
    def clickOnLearnMore(self):
        self.driver.find_element(By.CLASS_NAME,self.learnMoreLink).click()
    
    def getAllowAllButtonText(self):
        return self.driver.find_element(By.ID,self.acceptAll).text
 
    
    #Manage Consent Preferences
    def getManageConsentTitle(self):
        return self.driver.find_element(By.ID,self.manageTitle).text
    
    #Necessary Cookies
    
    def clickOnNecessaryCookiesGroup(self):
        self.driver.find_element(By.XPATH,self.necessaryCookiesGroup).click()

    def getNecessaryCookiesTitle(self):
        return self.driver.find_element(By.ID,self.necessaryCookiesLabel).text
    
    def getNecessaryCookiesDescription(self):
        return self.driver.find_element(By.ID,self.necessaryCookiesDescription).text

    def isNecessaryCookiesExpanded(self):
        return self.driver.find_element(By.XPATH,self.necessaryCookiesGroup).get_attribute("aria-expanded")
    
    def getNecessaryCookiesButtonText(self):
        return self.driver.find_element(By.CLASS_NAME,self.necessaryCookiesButton).text

    #Performance Cookies
    def clickOnPerformanceCookiesGroup(self):
        self.driver.find_element(By.XPATH,self.performanceCookiesGroup).click()    
        
    def isPerformanceCookiesExpanded(self):
        return self.driver.find_element(By.XPATH,self.performanceCookiesGroup).get_attribute("aria-expanded")
    
    def getPerformanceCookiesTitle(self):
        return self.driver.find_element(By.ID,self.performanceCookiesLabel).text
    
    def getPerformanceCookiesDescription(self):
        return self.driver.find_element(By.ID,self.performanceCookiesDescription).text
    
    def clickOnPerformanceCheckbox(self):
        self.driver.find_element(By.XPATH,self.performanceCookiesCheckbox).click()

    def isPerformanceCheckboxChecked(self):
        return self.driver.find_element(By.XPATH,self.performanceCookiesCheckbox).get_attribute("aria-checked")
    
    #Functional    
    def clickOnFunctionalCookiesGroup(self):
        self.driver.find_element(By.XPATH,self.functionalCookiesGroup).click()    
        
    def isFunctionalCookiesExpanded(self):
        return self.driver.find_element(By.XPATH,self.functionalCookiesGroup).get_attribute("aria-expanded")
    
    def getFunctionalCookiesTitle(self):
        return self.driver.find_element(By.ID,self.functionalCookiesLabel).text
    
    def getFunctionalCookiesDescription(self):
        return self.driver.find_element(By.ID,self.functionalCookiesDescription).text
    
    def clickOnFunctionalCheckbox(self):
        self.driver.find_element(By.ID,self.functionalCookiesCheckbox).click()

    def isFunctionalCheckboxChecked(self):
        return self.driver.find_element(By.ID,self.functionalCookiesCheckbox).get_attribute("aria-checked")

    #Targetting
    def clickOnTargettingCookiesGroup(self):
        self.driver.find_element(By.XPATH,self.targettingCookiesGroup).click()    
        
    def isTargettingCookiesExpanded(self):
        return self.driver.find_element(By.XPATH,self.targettingCookiesGroup).get_attribute("aria-expanded")
    
    def getTargettingCookiesTitle(self):
        return self.driver.find_element(By.ID,self.targettingCookiesLabel).text
    
    def getTargettingCookiesDescription(self):
        return self.driver.find_element(By.ID,self.targettingCookiesDescription).text
    
    def clickOnTargettingCheckbox(self):
        self.driver.find_element(By.ID,self.targettingCookiesCheckbox).click()

    def isTargettingCheckboxChecked(self):
        return self.driver.find_element(By.ID,self.targettingCookiesCheckbox).get_attribute("aria-checked")

    #Bottom Buttons
    def getRejectAllButtonText(self):
        return self.driver.find_element(By.CLASS_NAME,self.rejectAll).text
    
    def getSaveChoicesButtonText(self):
        return self.driver.find_element(By.CLASS_NAME,self.saveChoices).text
    
    
    
   