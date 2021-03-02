from bs4 import BeautifulSoup as bs

class exchange:
    def __init__(self, processEngine, IX):
        self.processEngine = processEngine
        self.processEngine.get("https://bgp.he.net/exchange/" + IX)
        self.webData = bs(self.processEngine.page_source,"html.parser")
        self.members = exchange.members(self)
        self.region = exchange.region(self)
        self.city = exchange.city(self)
        self.IPv4Prefixes = exchange.IPv4Prefixes(self)
        self.IPv6Prefixes = exchange.IPv6Prefixes(self)
        self.ISP(self)