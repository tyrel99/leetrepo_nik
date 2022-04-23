class Codec:

    def encode(self, longUrl: str) -> str:
        self.encodemap = {}
        self.decodemap = {}
        self.base = "https://tinyurl.com/"
        
        if longUrl not in self.encodemap:
            shortUrl = self.base + str(len(self.encodemap)+1)
            self.encodemap[longUrl] = shortUrl
            self.decodemap[shortUrl] = longUrl
            return self.encodemap[longUrl]
        """Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        return self.decodemap[shortUrl]
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))