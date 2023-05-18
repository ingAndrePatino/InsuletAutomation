import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.insulet.com/"

class CookiesBannerPage:
    def __init__(self,driver):
        self.driver = driver;    
        #Element identifiers.
        ##Cookies PopUp
        self.cookiesTitle = "onetrust-policy-title"
        self.cookiesText = "onetrust-policy-text"
        self.cookiesContinueWithoutAccepting = "banner-close-button"
        self.cookiesAcceptAll = "onetrust-accept-btn-handler"
        self.cookiesRejectAll = "onetrust-reject-all-handler"
        self.cookiesSettings = "onetrust-pc-btn-handler"
        

    
    
    def getBaseUrl(self):
        return base_url
    
    # Cookies Pop Up
    
    def getCookiesTitleText(self):
        return self.driver.find_element(By.ID,self.cookiesTitle).text
    
    def getCookiesDescriptionText(self):
        return self.driver.find_element(By.ID,self.cookiesText).text
    
    def getContinueWithoutAcceptingText(self):
        return self.driver.find_element(By.CLASS_NAME, self.cookiesContinueWithoutAccepting).text
    
    def clickOnContinueWithoutAcceptingText(self):
        self.driver.find_element(By.CLASS_NAME, self.cookiesContinueWithoutAccepting).click
    
    def clickOnAcceptAllCookies(self):
        self.driver.find_element(By.ID,self.cookiesAcceptAll).click()
    
    def getAcceptAllCookiesText(self):
        return self.driver.find_element(By.ID,self.cookiesAcceptAll).text
    
    def clickOnRejectAllCookies(self):
        self.driver.find_element(By.ID,self.cookiesRejectAll).click()
    
    def getRejectAllCookiesText(self):
        return self.driver.find_element(By.ID,self.cookiesRejectAll).text
    
    def getConfigureCookiesText(self):
        return self.driver.find_element(By.ID,self.cookiesSettings).text

        
    def clickOnConfigureCookies(self):
        self.driver.find_element(By.ID,self.cookiesSettings).click()
