from bs4 import BeautifulSoup as bs

class country:
    def __init__(self, processEngine, countryCode):
        self.processEngine = processEngine
        self.processEngine.get("https://bgp.he.net/country/" + countryCode)
        self.webData = bs(self.processEngine.page_source,"html.parser")
        self.ISP = country.ISP(self)
    def ISP(self):
        data = []
        datap1 = self.webData.find("tbody").find_all("tr")
        for i in datap1:
            datap2 = i.find("a").text
            datap3 = i.find_all("td")
            outdata = [datap2]
            del datap3[0]
            for p in datap3:
                outdata.append(p.text)
            data.append(outdata)
        return data
