from bs4 import BeautifulSoup as bs

class IPAddress:
    def __init__(self, processEngine, IP):
        self.processEngine = processEngine
        self.processEngine.get("https://bgp.he.net/ip/" + IP)
        self.webData = bs(self.processEngine.page_source,"html.parser")
        self.DNS = IPAddress.DNS(self)
        self.ISP = IPAddress.ISP(self)
    def DNS(self):
        data = self.webData.find("div", id="ipinfo").find("a").text
        return data
    def ISP(self):
        data = self.webData.find("div", id="ipinfo").find("table").find("tbody").find_all("tr")
        out = []
        for i in data:
            proc = i.find_all("td")
            ASN = proc[0].find("a").text
            announceIP = proc[1].find("a").text
            name = proc[2].text
            out.append([ASN, announceIP,name])
        return out