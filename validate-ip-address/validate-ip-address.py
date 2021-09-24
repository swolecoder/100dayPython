class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        def IPv4(s):
            try:
                
                return str(int(s)) ==s and 0 <= int(s) <= 255
            except:
                return False
        def IPv6(s):
            if len(s) > 4 or re.match("\W",s):
                return False
            
            try:
                int(s,16)
                return True
            except:
                return False
            
        
        ip4 = IP.split(".")
        ip6 = IP.split(":")
        
        if len(ip4) == 4 and all(IPv4(n) for n in ip4):
            return "IPv4"
        
        if len(ip6) == 8 and all(IPv6(n) for n in ip6):
            return "IPv6"
    
        return "Neither"
        