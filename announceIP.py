from bs4 import BeautifulSoup as bs

class announceIP:
    def __init__(self, processEngine, announcedIP):
        self.processEngine = processEngine
        self.processEngine.get("https://bgp.he.net/net/" + announcedIP)
        self.webData = bs(self.processEngine.page_source,"html.parser")
        self.ISP = announceIP.ISP(self)
    def ISP(self):
        data = self.webData.find("div", id="netinfo").find_all("table")[0].find_all("tbody")[-1].find("tr").find_all("td")
        ASN = data[0].find("a").text
        name = data[2].text
        return [ASN, name]
