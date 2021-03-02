from bs4 import BeautifulSoup as bs

class myself:
    def __init__(self, processEngine):
        self.processEngine = processEngine
        self.processEngine.get("https://bgp.he.net/")
        self.webData = bs(self.processEngine.page_source,"html.parser")
        self.IP = myself.IP(self)
        self.ISP = myself.ISP(self)
        self.announceIPs = myself.announceIPs(self)
        self.country = myself.country(self)
    def IP(self):
        data = self.webData.find_all("a", class_="boldlink")[0].text
        return data
    def ISP(self):
        data = self.webData.find_all("div")[-3].text.replace("\n","").replace("\t","").replace("Your ISP is ","").split(" ",1)
        datap2 = list(data[1])
        del datap2[0]
        del datap2[-1]
        del data[1]
        data.append("".join(datap2))
        data.append(self.webData.find_all("div")[-3].find("div", class_="flag alignright floatright").find("img").get("alt"))
        return data
    def announceIPs(self):
        proc = self.webData.find_all("div", class_="announcedas")
        data = []
        for i in proc:
            datap1 = i.text.replace("\n","").replace("\t","").replace("Announced as ","").split(" ",1)
            datap2 = list(datap1[1])
            del datap2[0]
            del datap2[-1]
            del datap1[1]
            datap1.append("".join(datap2))
            datap1.append(i.find("div", class_="flag alignright floatright").find("img").get("alt"))
            data.append(datap1)
        return data
    def country(self):
        data = self.webData.find("div", class_="flag alignright floatright").find("img").get("alt")
        return data
