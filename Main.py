from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
import random
from Self import *
from Country import *
from IPAddress import *
from announceIP import *
from Exchange import *
from ISPD import *

class BGPHENET:
    def __init__(self, path="phantomjs"):
        useragent = UserAgent(verify_ssl=False)
        #useragent.update()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap['phantomjs.page.settings.userAgent'] = useragent.random
        self.processEngine = webdriver.PhantomJS(executable_path=path,desired_capabilities=dcap)
    def MySelf(self):
        self.myself = myself(self.processEngine)
        return self.myself
    def Country(self, countryCode):
        self.country = country(self.processEngine, countryCode)
        return self.country
    def IP(self, IP):
        self.IPAddress = IPAddress(self.processEngine, IP)
        return self.IPAddress
    def AnnounceIP(self, announcedIP):
        self.announceIP = announceIP(self.processEngine, announcedIP)
        return self.announceIP
    def Exchange(self, IX):
        self.exchange = exchange(self.processEngine, IX)
        return self.exchange
    def ISP(self, ASN):
        self.ISPD = ISPD(self.processEngine, ASN)
        return self.ISPD