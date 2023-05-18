
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PageObject.Pages.CookiesBannerPage import CookiesBannerPage
from PageObject.Pages.PrivacyPreferenceCenterPage import PrivacyPreferenceCenterPage

class HomePageTests_Auto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.cookiesBannerPage = CookiesBannerPage(self.driver)
        self.preferenceCenterPage = PrivacyPreferenceCenterPage(self.driver)
        self.driver.maximize_window()

    def TestCookiesPopUpUI(self):
        cookiesBannerPage = self.cookiesBannerPage
        preferenceCenterPage = self.preferenceCenterPage
        
        driver = self.driver
        driver.get(cookiesBannerPage.getBaseUrl())
        
        #REQ1234: The popup shall show a message explaining to users what cookies are used for
        self.assertEqual(cookiesBannerPage.getCookiesTitleText(),"This website uses cookies")
        self.assertEqual(cookiesBannerPage.getCookiesDescriptionText(),"We use cookies to personalise content and ads, to provide social media features and to analyse our traffic. We also share information about your use of our site with our social media, advertising and analytics partners who may combine it with other information that you’ve provided to them or that they’ve collected from your use of their services. By clicking “Accept All Cookies”, you agree to the storing of cookies on your device to enhance site navigation, analyse site usage, and assist in our marketing efforts. By clicking on 'cookie settings' you can change your cookie preference")
        #REQ1235: The popup shall give the option to continue without accepting, accept all cookies, reject all cookies, or configure their own cookie settings 
        self.assertEqual(cookiesBannerPage.getContinueWithoutAcceptingText(),"Continue without Accepting")
        self.assertEqual(cookiesBannerPage.getAcceptAllCookiesText(),"Accept All Cookies")
        self.assertEqual(cookiesBannerPage.getRejectAllCookiesText(),"Reject All")       
        self.assertEqual(cookiesBannerPage.getConfigureCookiesText(),"Cookies Settings")
       
        #REQ1237: When the user clicks on the Cookies Settings Button, the privacy peference center popup shall appear  
        #REQ1238: The Privacy Preference Center popup shall include a description to the user about what cookies are, including a link to "Learn More"
        cookiesBannerPage.clickOnConfigureCookies()
        self.assertEqual(preferenceCenterPage.getTitle(),"Privacy Preference Center")
        self.assertEqual(preferenceCenterPage.getDescription(),"When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer.\nMore information")
        self.assertEqual(preferenceCenterPage.getLearnMoreText(),"More information")
        self.assertEqual(preferenceCenterPage.getAllowAllButtonText(),"Allow All")
        
        #REQ12349: The Privacy Preference Center popup shall include a section where the user is able to manage consent preferences
        self.assertEqual(preferenceCenterPage.getManageConsentTitle(),"Manage Consent Preferences")
        #REQ12349: The manage consent preferences section shall a description of all cookies type and a switch to accept or reject them
        #REQ12351: When the user clicks on any of the cookies types, an expanded description shall appear
        self.assertEqual(preferenceCenterPage.getNecessaryCookiesTitle(),"Strictly Necessary Cookies")
        self.assertEqual(preferenceCenterPage.isNecessaryCookiesExpanded(),"false")
        preferenceCenterPage.clickOnNecessaryCookiesGroup()
        self.assertEqual(preferenceCenterPage.isNecessaryCookiesExpanded(),"true")
        self.assertEqual(preferenceCenterPage.getNecessaryCookiesDescription(),"These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.")        
        self.assertEqual(preferenceCenterPage.getNecessaryCookiesButtonText(),"Always Active")

        
        self.assertEqual(preferenceCenterPage.getPerformanceCookiesTitle(),"Performance Cookies")
        self.assertEqual(preferenceCenterPage.isPerformanceCookiesExpanded(),"false")
        preferenceCenterPage.clickOnPerformanceCookiesGroup()
        self.assertEqual(preferenceCenterPage.isPerformanceCookiesExpanded(),"true")
        self.assertEqual(preferenceCenterPage.getPerformanceCookiesDescription(),"These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.")    
        self.assertEqual(preferenceCenterPage.isPerformanceCheckboxChecked(),"false")
        
        self.assertEqual(preferenceCenterPage.getFunctionalCookiesTitle(),"Functional Cookies")
        self.assertEqual(preferenceCenterPage.isFunctionalCookiesExpanded(),"false")
        preferenceCenterPage.clickOnFunctionalCookiesGroup()
        self.assertEqual(preferenceCenterPage.isFunctionalCookiesExpanded(),"true")
        self.assertEqual(preferenceCenterPage.getFunctionalCookiesDescription(),"Functional cookies are used to create technologically advanced and user-friendly websites that adapt automatically to your needs and preferences. These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.")
        self.assertEqual(preferenceCenterPage.isFunctionalCheckboxChecked(),"false")
        
        self.assertEqual(preferenceCenterPage.getTargettingCookiesTitle(),"Targeting Cookies")
        self.assertEqual(preferenceCenterPage.isTargettingCookiesExpanded(),"false")
        preferenceCenterPage.clickOnTargettingCookiesGroup()
        self.assertEqual(preferenceCenterPage.isTargettingCookiesExpanded(),"true")
        self.assertEqual(preferenceCenterPage.getTargettingCookiesDescription(),"These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.")
        self.assertEqual(preferenceCenterPage.isTargettingCheckboxChecked(),"false")
        
        #Bottom Buttons
        self.assertEqual(preferenceCenterPage.getRejectAllButtonText(),"Reject All")
        self.assertEqual(preferenceCenterPage.getSaveChoicesButtonText(),"Confirm My Choices")

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()  
        
if __name__ == "__main__":
    unittest.main()