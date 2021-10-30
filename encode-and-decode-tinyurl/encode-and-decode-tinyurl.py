class Codec:
    
    def __init__(self):
        self.encodemap = {}
        self.decodemap = {}
        self.url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        if longUrl not in self.encodemap:
            url = self.url + str(len(self.encodemap.values()) + 1)
            self.encodemap[longUrl] = url
            self.decodemap[url] = longUrl
            return url
        
        return self.encodemap[longUrl] 
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        if shortUrl not in self.decodemap:
            return ""
        
        return self.decodemap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))