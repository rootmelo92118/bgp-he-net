from bs4 import BeautifulSoup as bs

class ISPD:
    def __init__(self, processEngine, ASN):
        self.processEngine = processEngine
        self.processEngine.get("https://bgp.he.net/" + ASN)
        self.webData = bs(self.processEngine.page_source,"html.parser")
        self.info = exchange.info(self)
        self.IPv4Graphic = exchange.IPv4Graphic(self, savePath)
        self.IPv6Graphic = exchange.IPv6Graphic(self, savePath)
        self.IPv4Prefixes = exchange.IPv4Prefixes(self)
        self.IPv6Prefixes = exchange.IPv6Prefixes(self)
        self.IPv4Peers = exchange.IPv4Peers(self)
        self.IPv6Peers = exchange.IPv6Peers(self)
        self.exchange(self)